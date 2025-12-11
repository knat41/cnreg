# transform.py + tests

ด้านล่างเป็นเนื้อหาไฟล์สองไฟล์ที่คุณขอ: `transform.py` (โค้ดจริง) และชุดทดสอบ `tests/test_transform.py` (pytest)

คัดลอกไฟล์ทั้งสองไปไว้ในโปรเจกต์ของคุณ (เช่น root/) แล้วรัน `pytest` เพื่อตรวจ

---

## transform.py

```python
"""
transform.py

Contains getData2Frame(all_student_df, grade_level=None, ...) which:
- normalizes column names using constants.nameColumns or constants.CANONICAL_COLUMNS
- splits classroom into Class (grade) and Room
- normalizes StudentID to string zero-trimmed
- applies dtype hints from constants.dataTypeDict when possible
- optionally filters to a given grade_level (e.g., 3 for ม.3) and returns that subset

This module is defensive and does not perform file I/O.
"""
from typing import Optional, Dict, Any
import pandas as pd
import numpy as np

import constants


def _rename_columns(df: pd.DataFrame, mapping: Optional[Dict[str, str]] = None) -> pd.DataFrame:
    """Rename columns using mapping (case-insensitive keys are supported).
    mapping maps original-language or messy names -> canonical English names.
    If mapping is None, uses constants.nameColumns if present, else constants.CANONICAL_COLUMNS.
    """
    if mapping is None:
        mapping = getattr(constants, "nameColumns", None) or constants.CANONICAL_COLUMNS
    # build case-insensitive map from lowercased source -> target
    lowered_map = {k.lower(): v for k, v in mapping.items()}

    new_cols = {}
    for col in df.columns:
        key = col.lower()
        if key in lowered_map:
            new_cols[col] = lowered_map[key]
        else:
            # try strip whitespace and match
            key2 = col.strip().lower()
            if key2 in lowered_map:
                new_cols[col] = lowered_map[key2]
            else:
                # keep original
                new_cols[col] = col
    return df.rename(columns=new_cols)


def _split_classroom(df: pd.DataFrame, classroom_col: str = "Classroom") -> pd.DataFrame:
    """Split classroom into 'Class' (grade level numeric) and 'Room' if possible.
    Typical input examples: 'ม.3/2', '3/2', 'M3-2', 'ม.3'
    """
    if classroom_col not in df.columns:
        return df

    def parse_cl(x):
        if pd.isna(x):
            return (None, None)
        s = str(x).strip()
        # common Thai format 'ม.3/1' or 'ม.3' - find digit after 'ม.'
        try:
            # if contains '/': split
            if '/' in s:
                parts = [p.strip() for p in s.split('/') if p.strip()]
                # try to find grade in first part
                left = parts[0]
                # extract digits
                import re
                m = re.search(r"(\d+)", left)
                grade = int(m.group(1)) if m else None
                room = parts[1] if len(parts) > 1 else None
                return (grade, room)
            else:
                import re
                m = re.search(r"(\d+)", s)
                grade = int(m.group(1)) if m else None
                return (grade, None)
        except Exception:
            return (None, None)

    parsed = df[classroom_col].apply(parse_cl)
    df = df.copy()
    df["Class"] = parsed.map(lambda t: t[0])
    df["Room"] = parsed.map(lambda t: t[1])
    return df


def _apply_dtypes(df: pd.DataFrame, dtype_map: Optional[Dict[str, str]] = None) -> pd.DataFrame:
    """Attempt to cast columns according to dtype_map. Silently skip errors.
    dtype_map values should be pandas dtype strings, e.g. 'float32', 'int64', 'string'
    """
    if dtype_map is None:
        dtype_map = getattr(constants, "dataTypeDict", {})
    df = df.copy()
    for col, dtype in dtype_map.items():
        if col in df.columns:
            try:
                # use pandas astype where possible
                # for integer conversion, coerce errors to NaN then convert if desired
                if dtype.startswith("int"):
                    df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
                elif dtype.startswith("float"):
                    df[col] = pd.to_numeric(df[col], errors="coerce").astype(dtype)
                elif dtype in ("string", "str"):
                    df[col] = df[col].astype(object).where(pd.notnull(df[col]), None).astype("string")
                else:
                    # fallback to pandas astype
                    df[col] = df[col].astype(dtype, errors="ignore")
            except Exception:
                # skip casting on failure
                continue
    return df


def getData2Frame(all_student: pd.DataFrame,
                   grade_level: Optional[int] = None,
                   rename_mapping: Optional[Dict[str, str]] = None,
                   classroom_col: str = "Classroom",
                   student_id_col: str = "StudentID",
                   credits_col: str = "Credits") -> pd.DataFrame:
    """
    Clean and normalize raw combined DataFrame (all_student) and return cleaned DataFrame.

    Parameters
    ----------
    all_student : pd.DataFrame
        Raw dataframe concatenated from input files.
    grade_level : Optional[int]
        If provided, filter rows to this grade level (e.g., 3 for ม.3). Filtering uses the parsed
        'Class' value after splitting classroom. If None, no grade filtering applied.
    rename_mapping : Optional[Dict[str,str]]
        Mapping for renaming columns. If None, constants.nameColumns will be used.
    classroom_col : str
        Column name (after rename) that contains classroom info.
    student_id_col : str
        Column name for student id to normalize to string.
    credits_col : str
        Column name for credits. If absent, not added.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe ready for downstream processing.
    """
    if all_student is None:
        return pd.DataFrame()
    if not isinstance(all_student, pd.DataFrame):
        raise ValueError("all_student must be a pandas DataFrame")

    df = all_student.copy()

    # 1) Rename columns
    df = _rename_columns(df, mapping=rename_mapping)

    # 2) Normalize StudentID to string (strip, zero-pad not done automatically)
    if student_id_col in df.columns:
        df[student_id_col] = df[student_id_col].astype(str).str.strip().replace({'nan': None})
        # convert numeric-looking to int-like strings without decimals
        def _norm_id(v):
            if pd.isna(v) or v is None:
                return None
            s = str(v).strip()
            # remove fractional .0 if present
            if s.endswith('.0'):
                s = s[:-2]
            return s
        df[student_id_col] = df[student_id_col].map(_norm_id)

    # 3) Split classroom into Class and Room
    df = _split_classroom(df, classroom_col=classroom_col)

    # 4) Apply dtype hints where possible
    df = _apply_dtypes(df, dtype_map=getattr(constants, 'dataTypeDict', None))

    # 5) Drop fully empty rows (all NaN)
    df = df.dropna(how='all')

    # 6) Optionally filter by grade_level
    if grade_level is not None and 'Class' in df.columns:
        try:
            df = df[df['Class'] == int(grade_level)]
        except Exception:
            # if cannot filter, return empty set
            df = df.iloc[0:0]

    # 7) Reset index
    df = df.reset_index(drop=True)

    return df


# If run directly, run a small sanity check
if __name__ == "__main__":
    sample = pd.DataFrame([
        {"รหัสประขำตัว": 44132, "ชื่อ-นามสกุล": "สมชาย ใจดี", "ชั้น/ห้อง": "ม.3/2", "หน่วยกิต": 3},
        {"รหัสประขำตัว": 44133, "ชื่อ-นามสกุล": "สมหญิง ดีใจ", "ชั้น/ห้อง": "ม.4/1", "หน่วยกิต": 2},
    ])
    print(getData2Frame(sample, grade_level=3))
```

---

## tests/test_transform.py

```python
# tests/test_transform.py
import pandas as pd
from transform import getData2Frame, _rename_columns, _split_classroom, normalize_missing


def test_rename_and_split():
    raw = pd.DataFrame([
        {"รหัสประขำตัว": 1, "ชื่อ-นามสกุล": "ก ข", "ชั้น/ห้อง": "ม.3/1", "หน่วยกิต": "3"},
        {"รหัสประขำตัว": 2, "ชื่อ-นามสกุล": "ค ง", "ชั้น/ห้อง": "3/2", "หน่วยกิต": 2},
    ])
    df = getData2Frame(raw, grade_level=3)
    # after rename, columns should include StudentID, Name, Classroom
    assert 'StudentID' in df.columns
    assert 'Name' in df.columns or 'fullname' in df.columns
    # class parsed
    assert 'Class' in df.columns and 'Room' in df.columns
    assert set(df['Class'].dropna().astype(int).unique()) == {3}


def test_normalize_studentid_and_types():
    raw = pd.DataFrame([
        {"รหัสประขำตัว": 100.0, "ชื่อ-นามสกุล": "A", "ชั้น/ห้อง": "ม.3/2", "หน่วยกิต": "3"},
    ])
    df = getData2Frame(raw)
    assert df.loc[0, 'StudentID'] == '100'
    # credits should be numeric or Int64
    assert 'Credits' in df.columns
    assert pd.api.types.is_integer_dtype(df['Credits']) or pd.api.types.is_float_dtype(df['Credits'])
```

Notes:
- The tests assume pytest. Install pytest and run `pytest -q` in project root.
- If you have different column names, adjust the mapping in constants.py or pass rename_mapping to getData2Frame.

---

### Next steps (suggested)
- I can write these two files into your project directory (create physical files) if you want — บอกผมว่าให้ "เขียนไฟล์" และผมจะสร้างไฟล์จริง ๆ ให้ใน canvas / project filesystem.
- หรือต้องการปรับ mapping names in constants.py ก่อนทดสอบ ให้แจ้งรายการ columns ที่ใช้จริงมาได้เลย.

