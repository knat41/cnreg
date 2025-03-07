column_mapping = {
    "รหัสโรงเรียน": "school_id",
    "ชั้น/ห้อง": "class_section",
    "เลขประจำตัวนักเรียน": "student_id",
    "คำนำหน้า": "prefix",
    "ชื่อ": "first_name",
    "นามสกุล": "last_name",
    "เลขประจำตัวประชาชน": "national_id",
    "วันเกิด": "birth_date",
    "เพศ": "gender",
    "สัญชาติ": "nationality",
    "ศาสนา": "religion",
    "เชื่อชาติ": "ethnicity",
    "บิดา": "father_name",
    "เลขประชาชนบิดา": "father_national_id",
    "มารดา": "mother_name",
    "เลขประชาชนมารดา": "mother_national_id",
    "ผู้ปกครอง": "guardian",
    "ระดับชั้น": "grade_level",
    "ปีที่เข้า": "admission_year",
    "ภาคเรียนที่": "semester",
    "วันที่เข้า": "admission_date",
    "เข้าเรียนชั้น": "entry_grade",
    "โรงเรียนเดิม": "previous_school",
    "จังหวัด": "province",
    "จบการศึกษาระดับ": "graduation_level"
}

prefix_pattern = r'^(นาย|นางสาว|นาง|พล.ต.ท.|เด็กชาย|เด็กหญิง|ดร.|คุณ|ร.ต.|ร.อ.|ร.ท.|พล.อ.|พล.ต.อ.)'


def split_prefix(full_name):
    prefix_pattern = r'^(นาย|นางสาว|นาง|พล.ต.ท.|เด็กชาย|เด็กหญิง|ดร.|คุณ|ร.ต.|ร.อ.|ร.ท.|พล.อ.|พล.ต.อ.)'
    match = re.match(prefix_pattern, full_name)
    if match:
        prefix = match.group(0)
        name_without_prefix = full_name[len(prefix):].strip()
        return prefix, name_without_prefix
    else:
        return None, full_name  # ถ้าไม่มีคำนำหน้า