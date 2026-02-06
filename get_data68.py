import pandas as pd

# ถ้าเป็นไฟล์ .csv
# df = pd.read_csv("student_data.csv", encoding="utf-8")  # หรือ 'cp874' สำหรับภาษาไทย

# ถ้าเป็นไฟล์ .xlsx
df = pd.read_excel("2568-1-student.xlsx", header=1)

df = df.rename(columns={df.columns[2]: "เลขประจำตัวประชาชน"})
df = df.rename(columns={df.columns[5]: "เลขประจำตัวนักเรียน"})
# 1. ลบช่องว่างซ่อนในชื่อคอลัมน์
#df.columns = df.columns.str.strip()

# 2. ตรวจสอบคอลัมน์ที่ซ้ำ เช่น "เลขประจำตัวนักเรียน" ปรากฏ 2 ครั้ง
#df = df.loc[:, ~df.columns.duplicated()]

# 3. แปลงคอลัมน์วันที่ให้อยู่ในรูปแบบ datetime
#df["วันเกิด"] = pd.to_datetime(df["วันเกิด"], format="%d/%m/%Y", errors="coerce")
# แปลงวันเกิดจาก พ.ศ. เป็น ค.ศ.
def convert_thai_date(thai_date_str):
    try:
        d, m, y = map(int, thai_date_str.split('/'))
        y -= 543
        return pd.Timestamp(year=y, month=m, day=d)
    except:
        return pd.NaT

df["วันเกิด"] = df["วันเกิด"].apply(convert_thai_date)
# 4. แปลงอายุให้เป็นเลขจำนวนเต็ม
#df["อายุ(ปี)"] = pd.to_numeric(df["อายุ(ปี)"], errors="coerce")

# 5. เปลี่ยนชื่อคอลัมน์บางอันให้ใช้งานง่ายขึ้น (ถ้าต้องการ)
df = df.rename(columns={
    "รหัสโรงเรียน": "school_code",
    "ชื่อโรงเรียน": "school_name",
    "เลขประจำตัวประชาชน": "personal_id",    
    "ชั้น": "grade_level",
    "ห้อง": "classroom",
    "เลขประจำตัวนักเรียน": "student_id",
    "เพศ": "gender",
    "คำนำหน้าชื่อ": "title",
    "ชื่อ": "first_name",
    "นามสกุล": "last_name",
    "วันเกิด": "birth_date",
    "อายุ(ปี)": "age",
    "น้ำหนัก": "weight",
    "ส่วนสูง": "height",
    "กลุ่มเลือด": "blood_type",
    "ศาสนา": "religion",
    "เชื้อชาติ": "ethnicity",
    "สัญชาติ": "nationality",
    "บ้านเลขที่": "house_number",
    "หมู่": "village_number",
    "ถนน/ซอย": "street",
    "ตำบล": "sub_district",
    "อำเภอ": "district",
    "จังหวัด": "province",
    "ชื่อผู้ปกครอง": "guardian_first_name",
    "นามสกุลผู้ปกครอง": "guardian_last_name",
    "อาชีพของผู้ปกครอง": "guardian_occupation",
    "ความเกี่ยวข้องของผู้ปกครองกับนักเรียน": "guardian_relationship",
    "ชื่อบิดา": "father_first_name",
    "นามสกุลบิดา": "father_last_name",
    "อาชีพของบิดา": "father_occupation",
    "ชื่อมารดา": "mother_first_name",
    "นามสกุลมารดา": "mother_last_name",
    "อาชีพของมารดา": "mother_occupation",
    "ความด้อยโอกาส": "disadvantaged_status",
    "ยังไม่สามารถจำหน่ายได้ (3.1.8)": "not_discharged_3_1_8"
})

# 6. ตรวจสอบค่าหายหรือข้อมูลผิดปกติ (ยังไม่แสดงผล)
#missing_data = df.isnull().sum()

#กำหนดช่วงวันที่ (2552 = 2009, 2553 = 2010)
start_date = pd.Timestamp("2009-06-01")  # 1 มิ.ย. 2552
end_date = pd.Timestamp("2010-05-31")    # 31 พ.ค. 2553

# กรองเฉพาะนักเรียนที่เกิดในช่วงนี้
df_filtered = df[(df["birth_date"] >= start_date) & (df["birth_date"] <= end_date)]

selected_columns = [
    "student_id",     # เลขประจำตัวนักเรียน
    "grade_level",    # ชั้น
    "classroom",      # ห้อง
    "title",          # คำนำหน้าชื่อ
    "first_name",     # ชื่อ
    "last_name",      # นามสกุล
    "birth_date",      # วันเกิด (หลังแปลงแล้ว)
    "age"
]

df_selected = df_filtered[selected_columns]
df_selected.to_excel("selected_students.xlsx", index=False)
df.to_excel("all_students.xlsx", index=False)
