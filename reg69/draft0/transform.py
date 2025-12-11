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
print(getData2Frame(sample, grade_level=3))
