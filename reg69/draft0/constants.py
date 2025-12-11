"""
constants.py

Auto-generated constants extracted from cn_var.py (for compatibility).
KEEP THIS IN SYNC with your original cn_var.py if you edit that file.
"""
from typing import List, Dict, Any

# ---------------------------
# Environment / basic values
# ---------------------------
fpath = ''
path = 'data'
current_year = 2568
m = [1, 2, 3, 4, 5, 6]

ldir: List[str] = []

# cn gpa
cnsGPA = 0.0

# ---------------------------
# School / people
# ---------------------------
cnschool = ["ชลกันยานุกูล", "บางปลาสร้อย", "เมืองชลบุรี", "ชลบุรี"]
registrar = "นางสาววันวิสา ถุงทรัพย์"
director = "นางนภาพร  มูลเมือง"

# ---------------------------
# Column name mapping (nameColumns from cn_var.py)
# ---------------------------
nameColumns: Dict[str, str] = {
    "รหัสวิชา": "CourseID",
    "ชื่อวิชา": "Title",
    "หน่วยกิต": "Credits",
    "กลุ่มที่": "SectionCourseID",
    "ปีการศึกษา": "AcademicYear",
    "ภาคเรียนที่": "Semester",
    "ครูผู้สอน": "Instructor",
    "เลขประขำตัว": "StudentID",
    "ชื่อ-นามสกุล": "Name",
    "ชั้น/ห้อง": "Classroom",
    "เลขที่": "ClassNumber",
    "กลางภาค": "MidtermExam",
    "ปลายภาค": "FinalExam",
    "หลังกลางภาค": "FinalFormative",
    "ก่อนกลางภาค": "MidtermFormative",
    "รวม": "TotalScore",
    "รวมร้อยละ": "PercentScore",
    "ผลการเรียน": "Grade",
    "เต็มรวม": "FullMarks",
    "เต็มก่อนกลางภาค": "MidForFullMarks",
    "เต็มหลังกลางภาค": "FinForFullMarks",
    "เต็มกลางภาค": "MidFullMarks",
    "เต็มปลายภาค": "FinFullMarks",
}

# ---------------------------
# classDict (grade-level mapping)
# ---------------------------
classDict: Dict[str, int] = {
    'ม.1': 1,
    'ม.2': 2,
    'ม.3': 3,
    'ม.4': 4,
    'ม.5': 5,
    'ม.6': 6,
}

# ---------------------------
# dataTypeDict (as in cn_var.py)
# ---------------------------
dataTypeDict: Dict[str, str] = {
    'SectionCourseID': 'int8',
    'Credits': 'float32',
    'MidtermFormative': 'float32',
    'MidtermExam': 'float32',
    'FinalFormative': 'float32',
    'FinalExam': 'float32',
    'TotalScore': 'float32',
    'PercentScore': 'float32',
    'MidForFullMarks': 'float32',
    'MidFullMarks': 'float32',
    'FinForFullMarks': 'float32',
    'FinFullMarks': 'float32',
    'FullMarks': 'float32',
    'Class': 'float32',
    'Rooms': 'float32',
    'Q1': 'float32',
    'Q2': 'float32',
    'Q3': 'float32',
    'Q4': 'float32',
    'Q5': 'float32',
    'Q6': 'float32',
    'Q7': 'float32',
    'Q8': 'float32',
    'QGrade': 'float32',
    'L1': 'float32',
    'L2': 'float32',
    'L3': 'float32',
    'L4': 'float32',
    'L5': 'float32',
    'LGrade': 'float32',
}

# ---------------------------
# Learning group mapping
# ---------------------------
nLearningGroup: Dict[int, str] = {
    1: 'Thai Language',
    2: 'Mathematics',
    3: 'Science and Technology',
    4: 'Social Studies, Religion and Culture',
    5: 'Health and Physical Education',
    6: 'Arts',
    7: 'Occupations',
    8: 'Foreign Languages',
}

# ---------------------------
# Subject short codes (from cn_var)
# ---------------------------
classSubject = ['ท', 'ค', 'ส', 'ว', 'พ', 'ศ', 'ง', 'อ', 'ฝ', 'จ', 'ก', 'ญ']
activitySubject = ['A']

# ---------------------------
# Example text positions template extracted from cn_var.py
# This is the large text_positions array used to fill PDFs. Keep as-is.
# ---------------------------
text_positions: List[Any] = [
    ["ชลกันยานุกูล", (135, 661)], # ชื่อโรงเรียน
    ["บางปลาสร้อย", (400, 661)], #
    ["เมืองชลบุรี", (135, 634)],   #
    ["ชลบุรี", (400, 634)],
    ["นางฟ้า บนดอกบัวบาน", (330, 607)], # ชื่อ - นามสกุล
    ["44444", (160, 580)], # รหัสประจำตัวนักเรียน
    ["มัธยมศึกษาปีที่ 3", (330, 580)], 
    ["4.00", (415, 526)], # เกรดเฉลี่ยสะสม (gpax)
    ["4.00", (239, 410)], # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.1 เทอม 1)
    ["4.00", (296, 410)], # ... continued
    ["4.00", (353, 410)],
    ["4.00", (409, 410)],
    ["4.00", (466, 410)],
    ["4.00", (526, 410)],
    ["4.00", (239, 374)],
    ["4.00", (296, 374)],
    # The original file contains many more entries; keep this as a starting excerpt.
]

# ---------------------------
# Export list / defaults
# ---------------------------
DEFAULTS = {
    'parquet_engine': 'fastparquet',
    'gpa_decimals': 2,
    'grade_snap_tol': 1e-8,
}

__all__ = [
    'fpath', 'path', 'current_year', 'm', 'ldir', 'cnsGPA',
    'cnschool', 'registrar', 'director',
    'nameColumns', 'classDict', 'dataTypeDict', 'nLearningGroup',
    'classSubject', 'activitySubject', 'text_positions', 'DEFAULTS'
]
