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

def prePareData(path):
    import pandas as pd
    import glob
    dflist = []    
    print('Start creating dataframe')
    print('....')
    creadfile = 0
    fpath = './' + path + '/*.xlsx'  # หาไฟล์ .xls ในโฟลเดอร์ที่กำหนด
    print('Reading files...')
    
    ldir = glob.glob(fpath)  # ค้นหาไฟล์ทั้งหมด
    nfile = len(ldir)  # จำนวนไฟล์ที่พบ
    
    print(f'Found {nfile} .xls files')
    
    for data in ldir:
        print(f'Trying to read file: {data}')        
        try:
            # ใช้ engine='xlrd' สำหรับไฟล์ .xls (Excel เก่า)
            #dfm = pd.read_excel(data, engine='xlrd')
            df = pd.read_excel(data, engine="openpyxl")
            dflist.append(df)
            creadfile += 1
            print(f'{creadfile}/{nfile} files read ({(creadfile/nfile)*100:.2f}%) complete')

        except Exception as e:
            print(f'❌ Error reading file {data}: {e}')

    # รวมทุก DataFrame เข้าด้วยกัน
    if dflist:
        all_data = pd.concat(dflist, ignore_index=True)
        print('Dataframe created successfully!')
        return all_data
    else:
        print('No valid data found!')
        return None

def school_clean(df):
    # ลบคอลัมน์แรกที่ไม่มีชื่อ (index 0)
    df = df.drop(df.columns[0], axis=1)

    # เปลี่ยนชื่อคอลัมน์เป็นภาษาอังกฤษ
    df = df.rename(columns={
        "ชื่อโรงเรียน(ไทย)": "school_name_th",
        "ชื่อโรงเรียน(อังกฤษ)": "school_name_en",
        "ประเภทโรงเรียน": "school_type",
        "ลักษณะโรงเรียน": "school_characteristic",
        "จังหวัด": "province",
        "อำเภอ": "district",
        "ตำบล": "sub_district"
    })

    return df
    
def split_prefix(full_name):
    prefix_pattern = r'^(นาย|นางสาว|นาง|พล.ต.ท.|เด็กชาย|เด็กหญิง|ดร.|คุณ|ร.ต.|ร.อ.|ร.ท.|พล.อ.|พล.ต.อ.)'
    match = re.match(prefix_pattern, full_name)
    if match:
        prefix = match.group(0)
        name_without_prefix = full_name[len(prefix):].strip()
        return prefix, name_without_prefix
    else:
        return None, full_name  # ถ้าไม่มีคำนำหน้า