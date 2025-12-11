"""
gpa.py

Final GPA utility for numeric-only grade point system.

- Only numeric grade points are considered (allowed set default):
    [0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
  Any non-numeric or non-matching values (e.g., 'ร', 'มส', 'A') will be treated as NaN and excluded.

- compute_gpa and related functions compute weighted averages based on Credits.

- gpa_to_text(value, decimals=2) returns truncated string (not rounded),
  e.g. 3.897 -> "3.89".

Author: ChatGPT (for knat)
"""

from typing import Optional, List, Dict, Any, Union, Callable
import pandas as pd
import numpy as np
import math
from decimal import Decimal, ROUND_DOWN

# ---------- Configuration ----------
ALLOWED_GRADE_POINTS: List[float] = [0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]


# ---------- Helpers ----------

def normalize_grade_series(series: pd.Series,
                           allowed: Optional[List[float]] = None,
                           tol: float = 1e-8,
                           coerce_empty_to_nan: bool = True) -> pd.Series:
    """
    Normalize a series of grade values into floats that belong to the allowed set.
    - Accepts ints, floats, strings like "4", "4.0", " 3.5 ".
    - Non-numeric strings (e.g., 'ร', 'มส', 'A') -> NaN
    - Numeric values within `tol` of an allowed value will be snapped to that allowed float.
    - Returns a float Series with NaN for values that are not accepted.
    """
    allowed = allowed or ALLOWED_GRADE_POINTS
    allowed_arr = np.array(allowed, dtype=float)

    # Preprocess: convert empty strings to NaN if desired
    s = series.copy()
    # Convert pandas NA types to empty string first -> then coerce
    s = s.replace({None: np.nan})

    # Strip strings
    # Use astype(str) carefully: preserve NaN
    def strip_if_str(x):
        if pd.isna(x):
            return np.nan
        try:
            xs = str(x).strip()
            if xs == "":
                return np.nan if coerce_empty_to_nan else ""
            return xs
        except Exception:
            return np.nan

    s_stripped = s.map(strip_if_str)

    # coerce to numeric where possible
    numeric = pd.to_numeric(s_stripped, errors='coerce')

    # snap numeric values to allowed set within tolerance
    def snap_val(v):
        if pd.isna(v):
            return np.nan
        # v is numeric
        diffs = np.abs(allowed_arr - float(v))
        idx = int(np.argmin(diffs))
        if diffs[idx] <= tol:
            return float(allowed_arr[idx])
        # Optionally allow small fuzz (e.g., 0.01) to accommodate float inaccuracies:
        # if diffs[idx] <= 1e-2:
        #     return float(allowed_arr[idx])
        return np.nan

    snapped = numeric.map(snap_val)

    return snapped


def gpa_to_text(value: Optional[float], decimals: int = 2) -> str:
    """
    Truncate (not round) a float value to `decimals` decimal places and return as string.
    Examples:
        3.897 -> "3.89"
        3.899 -> "3.89"
        4.0   -> "4.00"
    Returns empty string for None or NaN.
    Implementation uses Decimal.quantize with ROUND_DOWN to ensure truncation.
    """
    if value is None:
        return ""
    try:
        if isinstance(value, float) and math.isnan(value):
            return ""
        # Use Decimal for precise truncation
        # Convert via string to avoid float repr issues
        d = Decimal(str(float(value)))
        if decimals <= 0:
            quant = Decimal('1')
        else:
            quant = Decimal('0.' + ('0' * (decimals - 1)) + '1')  # e.g. '0.01' for 2 decimals
        truncated = d.quantize(quant, rounding=ROUND_DOWN)
        fmt = f"{{0:.{decimals}f}}"
        return fmt.format(truncated)
    except Exception:
        # fallback string slicing
        try:
            s = f"{float(value):.10f}"
            dot = s.find(".")
            if dot == -1:
                return s
            return s[:dot + 1 + decimals]
        except Exception:
            return str(value)


# ---------- Core GPA computations ----------

def compute_gpa(df: pd.DataFrame,
                grade_col: str = "Grade",
                credits_col: str = "Credits",
                allowed_points: Optional[List[float]] = None,
                tol: float = 1e-8) -> Optional[float]:
    """
    Compute GPA for the provided DataFrame `df` using numeric-only grade values.

    - grade_col: column name for grade values (may be int/float or strings like "4" or "3.5")
    - credits_col: column name for credits (numeric). If missing, assume credits = 1 for each row.
    - allowed_points: allowed numeric grade points list (defaults to ALLOWED_GRADE_POINTS).
    - tol: tolerance for snapping numeric values to allowed points.

    Returns:
        float GPA value (not formatted) or None if no valid grades found.
    """
    if df is None or df.shape[0] == 0:
        return None

    allowed = allowed_points or ALLOWED_GRADE_POINTS

    if grade_col not in df.columns:
        return None

    grades_raw = df[grade_col]
    grades = normalize_grade_series(grades_raw, allowed=allowed, tol=tol)

    # parse credits
    if credits_col in df.columns:
        credits = pd.to_numeric(df[credits_col], errors='coerce').fillna(0.0)
    else:
        credits = pd.Series([1.0] * len(df), index=df.index)

    # valid rows: grade not NaN and credits > 0
    valid_mask = grades.notna() & (credits > 0)
    if not valid_mask.any():
        return None

    gp_vals = grades[valid_mask].astype(float)
    cred_vals = credits[valid_mask].astype(float)

    total_weighted = (gp_vals * cred_vals).sum()
    total_credits = cred_vals.sum()
    if total_credits == 0:
        return None

    return float(total_weighted / total_credits)


def compute_term_gpa(df: pd.DataFrame,
                     year: Optional[Union[int, str]] = None,
                     term: Optional[Union[int, str]] = None,
                     year_col: str = "Year",
                     term_col: str = "Term",
                     **kwargs) -> Optional[float]:
    """
    Compute GPA for a specific year and/or term by filtering df first.
    Passes kwargs to compute_gpa (grade_col, credits_col, allowed_points, tol).
    If year or term is None, that filter is ignored.
    """
    if df is None:
        return None
    mask = pd.Series([True] * len(df), index=df.index)
    if year is not None and year_col in df.columns:
        mask = mask & (df[year_col] == year)
    if term is not None and term_col in df.columns:
        mask = mask & (df[term_col] == term)
    sub = df[mask]
    return compute_gpa(sub, **kwargs)


def compute_gpa_by_group(df: pd.DataFrame,
                         student_id: Optional[Union[int, str]] = None,
                         group_filter: Optional[Union[str, Callable[[pd.DataFrame], pd.Series]]] = None,
                         student_col: str = "StudentID",
                         group_col: str = "Group",
                         **kwargs) -> Optional[float]:
    """
    Compute GPA filtered by a group. group_filter can be:
      - None: no group filtering
      - string: match group_col == string OR if group_col not present, try CourseID prefix match
      - callable: a function that accepts df and returns boolean mask
    If student_id provided, compute only for that student.
    """
    if df is None:
        return None
    mask = pd.Series([True] * len(df), index=df.index)
    if student_id is not None and student_col in df.columns:
        mask = mask & (df[student_col] == student_id)

    if group_filter is not None:
        if callable(group_filter):
            mask = mask & group_filter(df)
        elif isinstance(group_filter, str):
            if group_col in df.columns:
                mask = mask & (df[group_col] == group_filter)
            else:
                # try CourseID prefix
                course_col = None
                for cand in ["CourseID", "course_id", "courseid", "subject_code", "subject"]:
                    if cand in df.columns:
                        course_col = cand
                        break
                if course_col:
                    mask = mask & df[course_col].astype(str).str.startswith(group_filter)
                else:
                    # cannot filter
                    mask = mask & pd.Series([False] * len(df), index=df.index)
        else:
            raise ValueError("group_filter must be None, string, or callable")

    sub = df[mask]
    return compute_gpa(sub, **kwargs)


def compute_gpax(all_df: pd.DataFrame,
                  student_id: Union[int, str],
                  student_col: str = "StudentID",
                  **kwargs) -> Optional[float]:
    """
    Compute cumulative GPA (GPAX) for a given student across all rows in all_df.
    kwargs forwarded to compute_gpa (grade_col, credits_col, allowed_points, tol).
    """
    if all_df is None or student_id is None:
        return None
    if student_col in all_df.columns:
        student_rows = all_df[all_df[student_col] == student_id]
    else:
        student_rows = all_df
    return compute_gpa(student_rows, **kwargs)


# ---------- Student summary helpers ----------

def _infer_columns(df: pd.DataFrame) -> Dict[str, Optional[str]]:
    """
    Heuristic inference for common column names.
    Returns dict with keys: student_id, grade, credits, year, term, course_id, group, fullname, room
    """
    lower_map = {c.lower(): c for c in df.columns}
    def find_one(candidates: List[str]) -> Optional[str]:
        for cand in candidates:
            if cand.lower() in lower_map:
                return lower_map[cand.lower()]
        return None

    return {
        "student_id": find_one(["student_id", "id", "studentno", "student_no", "รหัสนักเรียน"]),
        "grade": find_one(["grade", "result", "score", "คะแนน"]),
        "credits": find_one(["credits", "credit", "หน่วยกิต", "cr"]),
        "year": find_one(["year", "academic_year", "ปีการศึกษา", "ปี"]),
        "term": find_one(["term", "semester", "ภาคเรียน"]),
        "course_id": find_one(["courseid", "course_id", "subject", "subject_code"]),
        "group": find_one(["group", "group_code", "subject_group", "กลุ่ม"]),
        "fullname": find_one(["fullname", "name", "student_name", "ชื่อ-นามสกุล", "ชื่อ"]),
        "room": find_one(["classroom", "room", "ห้อง", "class"]),
    }


def get_student_profile(df: pd.DataFrame,
                        student_id: Union[int, str],
                        student_col: str = "StudentID",
                        fullname_col: Optional[str] = None,
                        room_col: Optional[str] = None,
                        gpax_kwargs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Return profile dict for a student with gpax_text included.
    """
    if df is None:
        return {}
    cand = _infer_columns(df)
    sid_col = student_col if student_col in df.columns else cand.get("student_id") or student_col
    fullname_col = fullname_col or cand.get("fullname")
    room_col = room_col or cand.get("room")

    if sid_col in df.columns:
        rows = df[df[sid_col] == student_id]
    else:
        rows = df

    profile = {"student_id": student_id, "fullname": "", "room": ""}
    if fullname_col and fullname_col in rows.columns and len(rows) > 0:
        profile["fullname"] = str(rows.iloc[0][fullname_col])
    if room_col and room_col in rows.columns and len(rows) > 0:
        profile["room"] = str(rows.iloc[0][room_col])

    gpax_kwargs = gpax_kwargs or {}
    gpax_val = compute_gpax(df, student_id, **gpax_kwargs)
    profile["gpax_value"] = gpax_val
    profile["gpax_text"] = gpa_to_text(gpax_val, 2) if gpax_val is not None else ""

    return profile


def get_academic_summary(all_df: pd.DataFrame,
                         student_id: Union[int, str],
                         *,
                         subject_groups: Optional[Dict[str, Union[str, Callable[[pd.DataFrame], pd.Series]]]] = None,
                         student_col: str = "StudentID",
                         grade_col: str = "Grade",
                         credits_col: str = "Credits",
                         **gpa_kwargs) -> Dict[str, Any]:
    """
    Summarize academic info for PDF/report consumption:
    Returns dict with gpax_value, gpax_text, total_credits, gpa_by_group {name: {value, text}}
    subject_groups mapping name -> group_filter (string prefix or callable)
    """
    summary: Dict[str, Any] = {"student_id": student_id, "gpax_value": None, "gpax_text": "", "gpa_by_group": {}, "total_credits": 0.0}
    if all_df is None:
        return summary

    # base student rows
    if student_col in all_df.columns:
        student_rows = all_df[all_df[student_col] == student_id]
    else:
        student_rows = all_df

    gpax_val = compute_gpa(student_rows, grade_col=grade_col, credits_col=credits_col, **gpa_kwargs)
    summary["gpax_value"] = gpax_val
    summary["gpax_text"] = gpa_to_text(gpax_val, 2) if gpax_val is not None else ""

    # total credits
    if credits_col in student_rows.columns:
        try:
            summary["total_credits"] = float(pd.to_numeric(student_rows[credits_col], errors="coerce").fillna(0).sum())
        except Exception:
            summary["total_credits"] = 0.0
    else:
        summary["total_credits"] = float(len(student_rows))

    # groups
    if subject_groups:
        for name, gf in subject_groups.items():
            if callable(gf):
                mask = gf(student_rows)
                val = compute_gpa(student_rows[mask], grade_col=grade_col, credits_col=credits_col, **gpa_kwargs)
            elif isinstance(gf, str):
                # try prefix on CourseID
                course_col = None
                for cand in ["CourseID", "course_id", "courseid", "subject_code", "subject"]:
                    if cand in student_rows.columns:
                        course_col = cand
                        break
                if course_col:
                    mask = student_rows[course_col].astype(str).str.startswith(gf)
                    val = compute_gpa(student_rows[mask], grade_col=grade_col, credits_col=credits_col, **gpa_kwargs)
                elif "Group" in student_rows.columns:
                    mask = student_rows["Group"] == gf
                    val = compute_gpa(student_rows[mask], grade_col=grade_col, credits_col=credits_col, **gpa_kwargs)
                else:
                    val = None
            else:
                val = None
            summary["gpa_by_group"][name] = {"value": val, "text": gpa_to_text(val, 2) if val is not None else ""}

    return summary


# ---------- Self-test ----------
if __name__ == "__main__":
    # small example/demo
    demo = [
        {"StudentID": 1, "CourseID": "M101", "Credits": 3, "Grade": "4"},
        {"StudentID": 1, "CourseID": "M102", "Credits": 2, "Grade": 3.5},
        {"StudentID": 1, "CourseID": "HIST", "Credits": 1, "Grade": "มส"},  # to exclude
        {"StudentID": 2, "CourseID": "M101", "Credits": 3, "Grade": "4.0"},
        {"StudentID": 2, "CourseID": "ENG", "Credits": 2, "Grade": "3.5"},
        {"StudentID": 2, "CourseID": "ART", "Credits": 1, "Grade": "A"},  # excluded (non-numeric)
    ]
    df_demo = pd.DataFrame(demo)

    print("Normalized grades:")
    print(normalize_grade_series(df_demo["Grade"]))
    print("---")
    print("GPAX student 1 (float):", compute_gpax(df_demo, 1))
    print("GPAX student 1 (text):", gpa_to_text(compute_gpax(df_demo, 1), 2))
    print("GPAX student 2 (float):", compute_gpax(df_demo, 2))
    print("GPAX student 2 (text):", gpa_to_text(compute_gpax(df_demo, 2), 2))
