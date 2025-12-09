#subject
classSubject = ['ท', 'ค', 'ส', 'ว', 'พ', 'ศ', 'ง', 'อ', 'ฝ', 'จ', 'ก', 'ญ']
activitySubject = ['A']

nameColumns = {
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

classDict = {
    'ม.1' : 1,
    'ม.2' : 2,
    'ม.3' : 3,
    'ม.4' : 4,
    'ม.5' : 5,
    'ม.6' : 6
}
#
dataTypeDict = {
    'SectionCourseID':'int8',
    'Credits':'float32',
    'MidtermFormative' : 'float32',
    'MidtermExam' : 'float32',
    'FinalFormative' : 'float32',
    'FinalExam' : 'float32',
    'TotalScore' : 'float32',
    'PercentScore' : 'float32',
    'MidForFullMarks' : 'float32',
    'MidFullMarks' : 'float32',
    'FinForFullMarks' : 'float32',
    'FinFullMarks' : 'float32',
    'FullMarks' : 'float32',
    'Class':'float32',
    'Rooms':'float32',
    'Q1' : 'float32',
    'Q2' : 'float32',
    'Q3' : 'float32',
    'Q4' : 'float32',
    'Q5' : 'float32',
    'Q6' : 'float32',
    'Q7' : 'float32',
    'Q8' : 'float32',
    'QGrade' : 'float32',
    'L1' : 'float32',
    'L2' : 'float32',
    'L3' : 'float32',
    'L4' : 'float32',
    'L5' : 'float32',
    'LGrade' : 'float32'
}

nLearningGroup = {
    1: 'Thai Language',
    2: 'Mathematics',
    3: 'Science and Technology',
    4: 'Social Studies, Religion and Culture',
    5: 'Health and Physical Education',
    6: 'Arts',
    7: 'Occupations',
    8: 'Foreign Languages',
}

'''
1. Thai Language
2. Mathematics
3. Science and Technology
4. Social Studies, Religion and Culture
5. Health and Physical Education
6. Arts
7. Occupations 
8. Foreign Languages

Truncate at 2 Decimal Place
from math import floor
print(str(floor(0.5198 * 10**2) / 10**2))
'''
# chonkanya detail 
cnschool = ["ชลกันยานุกูล", "บางปลาสร้อย", "เมืองชลบุรี", "ชลบุรี"]
# Registra
registrar = "นางสาววันวิสา ถุงทรัพย์"
director = "นางนภาพร  มูลเมือง"

fpath = ''
path = 'data'
current_year = 2568
m = [1, 2, 3, 4, 5, 6]

ldir = []

# cn gpa
cnsGPA = 0.0

# ตัวอย่างตำแหน่งข้อความ (x, y) บน PDF
text_positions = [
    ["ชลกันยานุกูล", (135, 661)], # ชื่อโรงเรียน
    ["บางปลาสร้อย", (400, 661)], #
    ["เมืองชลบุรี", (135, 634)],   #
    ["ชลบุรี", (400, 634)],
    ["นางฟ้า บนดอกบัวบาน", (330, 607)], # ชื่อ - นามสกุล
    ["44444", (160, 580)], # รหัสประจำตัวนักเรียน
    ["มัธยมศึกษาปีที่ 3", (330, 580)], 
    ["4.00", (415, 526)], # เกรดเฉลี่ยสะสม (gpax)
    ["4.00", (239, 410)], # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.1 เทอม 1)
    ["4.00", (296, 410)], # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.1 เทอม 2)
    ["4.00", (353, 410)], # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.2 เทอม 1)
    ["4.00", (409, 410)], # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.2 เทอม 2)
    ["4.00", (466, 410)], # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.3 เทอม 1)
    ["4.00", (526, 410)], # เกรดเฉลี่ย กลุ่มสาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี รวม 5 ภาค
    ["4.00", (239, 374)], # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ (ม.1 เทอม 1)
    ["4.00", (296, 374)], # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ (ม.1 เทอม 2)
    ["4.00", (353, 374)], # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ (ม.2 เทอม 1)
    ["4.00", (409, 374)], # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ (ม.2 เทอม 2)
    ["4.00", (466, 374)], # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ (ม.3 เทอม 1)
    ["4.00", (526, 374)], # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ รวม 5 ภาค
    ["4.00", (239, 338)], # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ (ม.1 เทอม 1)
    ["4.00", (296, 338)], # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ (ม.1 เทอม 2)
    ["4.00", (353, 338)], # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ (ม.2 เทอม 1)
    ["4.00", (409, 338)], # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ (ม.2 เทอม 2)
    ["4.00", (466, 338)], # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ (ม.3 เทอม 1)
    ["4.00", (526, 338)], # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ รวม 5 ภาค
    ["นางสาววันวิสา ถุงทรัพย์", (115, 184)],
    ["นางนภาพร  มูลเมือง", (395, 220)],
    ["ผู้อำนวยการโรงเรียนชลกันยานุกูล", (384, 201)]
]

def make_cru1text_positions():
    column = [[175, 251, 320], [382, 457,528]]
    rows = [433, 415, 396, 379, 359, 341, 322, 305, 285, 266]
    points = [(150, 623), (330, 623), (495, 623), (200, 605), (110, 587), (260, 587), (400, 587),
              (375, 551), (261, 514), (418, 514)]
    for ncol in range(2):    
        for row in rows:
            for ecol in range(3):
                points.append((column[ncol][ecol], row))
    lastpoint = [(251, 248), (457, 248), (300, 172), (307, 100)]
    for point in lastpoint:
        points.append(point)
    cnschool = ["ชลกันยานุกูล", "บางปลาสร้อย", "เมืองชลบุรี", "ชลบุรี"]    
    cruposition = []
    for point in range(len(points)):
        if point in range(3, 7):
            cruposition.append([cnschool[point - 3], points[point]])        
        else:
            cruposition.append(["", points[point]])
    cruposition[-2][0] = "นางสาววันวิสา ถุงทรัพย์"
    cruposition[-1][0] = "นางนภาพร  มูลเมือง"    
    return cruposition

def make_cru3text_positions():
    column = [[228, 293, 355], [410, 477,535]]
    rows = [438, 420, 401, 384, 364, 346, 327, 310, 290, 273]
    points = [(150, 623), (330, 623), (495, 623), (200, 605), (110, 587), (260, 587), (400, 587),
              (375, 551), (413, 533)]
    for ncol in range(2):    
        for row in rows:
            for ecol in range(3):
                points.append((column[ncol][ecol], row))
    lastpoint = [(335, 238), (300, 182), (307, 110)]
    for point in lastpoint:
        points.append(point)
    cnschool = ["ชลกันยานุกูล", "บางปลาสร้อย", "เมืองชลบุรี", "ชลบุรี"]    
    cruposition = []
    for point in range(len(points)):
        if point in range(3, 7):
            cruposition.append([cnschool[point - 3], points[point]])        
        else:
            cruposition.append(["", points[point]])
    cruposition[-2][0] = "นางสาววันวิสา ถุงทรัพย์"
    cruposition[-1][0] = "นางนภาพร  มูลเมือง"
    return cruposition

def make_cru2text_positions():
    column = [[133, 190, 235], [280, 335, 381], [424, 480,527]]
    rows = [454, 437, 420, 405, 388, 371, 355, 339, 322, 306, 290, 273, 257, 240, 224]
    points = [(150, 653), (330, 653), (495, 653), (200, 635), (110, 617), (260, 617), (400, 617),
              (375, 581), (485, 563), (205, 545), (425, 545)]
    for ncol in range(3):    
        for row in rows:
            for ecol in range(3):
                points.append((column[ncol][ecol], row))
    lastpoint = [(190, 208), (335, 208), (480, 208), (297, 151), (305, 97)]
    for point in lastpoint:
        points.append(point)
    cnschool = ["ชลกันยานุกูล", "บางปลาสร้อย", "เมืองชลบุรี", "ชลบุรี"]    
    cruposition = []
    for point in range(len(points)):
        if point in range(3, 7):
            cruposition.append([cnschool[point - 3], points[point]])        
        else:
            cruposition.append(["", points[point]])
    cruposition[-2][0] = "นางสาววันวิสา ถุงทรัพย์"
    cruposition[-1][0] = "นางนภาพร  มูลเมือง"
    return cruposition

def fill_text_on_existing_pdf(input_pdf, output_pdf, text_positions, font_file="THSarabunNew.ttf", font_size=14):
    """
    เติมข้อความลงบน PDF เดิม (form_template.pdf) และบันทึกเป็น PDF ใหม่
    :param input_pdf: ไฟล์ PDF ต้นฉบับ
    :param output_pdf: ไฟล์ PDF ที่จะบันทึกข้อความใหม่
    :param text_positions: ลิสต์ของข้อความและตำแหน่ง [(ข้อความ, (x, y))]
    :param font_file: เส้นทางไปยังไฟล์ฟอนต์ .ttf
    :param font_size: ขนาดฟอนต์ (ค่าเริ่มต้น 14)    
    """
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.pagesizes import A4
    from PyPDF2 import PdfReader, PdfWriter
    from io import BytesIO
    
    # สร้าง PDF ชั่วคราวเพื่อวางข้อความ
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    pdfmetrics.registerFont(TTFont("THSarabun", font_file))
    can.setFont("THSarabun", font_size)
    
    # เติมข้อความในแต่ละตำแหน่ง
    for text, position in text_positions:
        can.drawString(position[0], position[1], text)
    
    can.save()
    packet.seek(0)

    # รวม PDF เดิมกับ PDF ที่มีข้อความใหม่
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    overlay_pdf = PdfReader(packet)

    for page_number in range(len(reader.pages)):
        page = reader.pages[page_number]
        if page_number == 0:  # วางข้อความเฉพาะหน้าแรก
            page.merge_page(overlay_pdf.pages[0])
        writer.add_page(page)
    
    # บันทึกเป็นไฟล์ใหม่
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    
    print(f"เติมข้อความสำเร็จ! บันทึกไว้ที่: {output_pdf}")

def getCRUmenu():
    print("Generating CRU certificate...")

    id_student = input("Enter Student ID: ").strip()

    if not dataframelist:
        print("No data available. Please load or create a datafile first.")
        return

    getCRUPDF(dataframelist, id_student)

def getCNmenu():
    print("Generating CN certificate...")
    
    # รับค่า Student ID จากผู้ใช้
    id_student = input("Enter Student ID: ").strip()

    # ตรวจสอบว่ามีไฟล์ข้อมูลหรือไม่
    if not dataframelist:
        print("No data available. Please load or create a datafile first.")
        return

    # เรียกใช้งาน getCNPDF พร้อมพารามิเตอร์
    getCNPDF(dataframelist, id_student)

def create_datafile():    
    print("Creating datafile...")
    all_student = prePareData(path)
    m3_student = getData2Frame(all_student)    
    m3_student.to_json('all66_m3.zip', orient = 'table', index = False, compression={'method': 'zip', 'compresslevel': 1})
    dfm = pd.read_html('GPA2567_1_m3.xls', encoding = 'utf-8')
    m3_data = pd.concat(dfm, ignore_index=True)
    m3_data.to_json('gpa67_m3.zip', orient = 'table', index = False, compression={'method': 'zip', 'compresslevel': 1})

    # เพิ่มโค้ดสำหรับสร้างข้อมูล

def load_datafile():
    import pandas as pd
    print("Loading datafile...")
    m3_student = pd.read_json('export66_m3.json', orient = 'table', compression={'method': 'zip', 'compresslevel': 1})
    gpa_m3 = pd.read_json('gpa67_m3.zip', orient = 'table', compression={'method': 'zip', 'compresslevel': 1})
    return [m3_student, gpa_m3]

def load_student_profiles():
    import pandas as pd
    import glob
    dflist = []    
    print('Start create dataframe')
    print('....')
    creadfile = 0
    path = 'profiles'
    fpath = './' + path + '/*.xls'
    print('Readding file')
    ldir = glob.glob(fpath)
    nfile = len(ldir)
    print(f'Found xls {nfile}')
    for data in ldir:
        print(f'Try to read file {data}')
        # To open an excel file with encoding utf-8 for read thai
        dfm = pd.read_html(data, encoding = 'utf-8')
        if len(list(dfm[0].select_dtypes(include=['object']))) == 46:
            #if header not 1st row try to read 2nd header
            dfm = pd.read_html(data, header = 1, encoding = 'utf-8')
        # append data frame to dataframe list
        dflist.append(dfm[0])
        creadfile += 1
        print(f'{creadfile}/{nfile} {(creadfile/nfile)*100:.2f} % complete')
    #combine all data frame        
    all_data = pd.concat(dflist, ignore_index=True)
    print('created done')
    
    return all_data

    
def prePareData(path):
    import pandas as pd
    import glob
    import os
    
    dflist = []    
    print('Start create dataframe')
    print('....')
    creadfile = 0
    fpath = os.path.join(".", path, "*.xls")
    print('Readding file')
    ldir = glob.glob(fpath)
    nfile = len(ldir)
    print(f'Found xls {nfile}')
    for data in ldir:
        print(f'Try to read file {data}')
        # To open an excel file with encoding utf-8 for read thai
        dfm = pd.read_html(data, encoding = 'utf-8')
        if len(list(dfm[0].select_dtypes(include=['object']))) == 46:
            #if header not 1st row try to read 2nd header
            dfm = pd.read_html(data, header = 1, encoding = 'utf-8')
        # append data frame to dataframe list
        dflist.append(dfm[0])
        creadfile += 1
        print(f'{creadfile}/{nfile} {(creadfile/nfile)*100:.2f} % complete')
    #combine all data frame        
    all_data = pd.concat(dflist, ignore_index=True)

    print('created done')
    
    return all_data

def getData2Frame(all_student):
    #Drop some columns
    all_student = all_student.drop(['รหัสโรงเรียน', 'Q9', 'Q10', 'เวลาเรียนร้อยละ', 'สาย', 'ลาป่วย', 'ลากิจ', 'ขาด'], axis = 1)
    print('drop columns')

    #Change columns name
    all_student.rename(columns = nameColumns, inplace=True)

    #Split columns 'classrooms' to class and rooms
    all_student[['Class', 'Rooms']] = all_student['Classroom'].str.split('/', expand = True)

    #Remap Values Directly on the 'Class'
    all_student['Class'] = all_student['Class'].replace(classDict)

    #Converting 2 columns to int
    all_student = all_student.astype({'Class':'int8', 'Rooms':'int8'})
    all_student = all_student.drop(['Classroom'], axis = 1)
    all_student = all_student.astype(dataTypeDict)

    #Select columns with out activity
    condition_1 = all_student['CourseID'].str.contains(".*A.*")
    condition_2 = all_student['CourseID'] == 'I30903'
    dfs = all_student[(~condition_1) & (~condition_2)]
    return dfs

def getDFAS(dataframe, id_student, year, term, subj, stype):
    match stype:
        # for basic course
        case 1:
                qtext = (
        "StudentID == "
        + str(id_student)
        + " and "
        + "AcademicYear == "
        + str(year)
        + " and "
        + "Semester == "
        + str(term)
        + " and "
        + "CourseID.str.contains('[" + subj + "]\d\d[1]\d\d')"
    )
        # for additional course
        case 2:
                qtext = (
        "StudentID == "
        + str(id_student)
        + " and "
        + "AcademicYear == "
        + str(year)
        + " and "
        + "Semester == "
        + str(term)
        + " and "
        + "CourseID.str.contains('[" + subj + "]\d\d[2]\d\d')"
    )
        # for all course
        case 3:
                qtext = (
        "StudentID == "
        + str(id_student)
        + " and "
        + "AcademicYear == "
        + str(year)
        + " and "
        + "Semester == "
        + str(term)
        + " and "
        + "CourseID.str.contains('[" + subj + "]\d\d\d\d\d')"
    )

    
    s1 = dataframe.query(qtext)
    s1 = s1.astype({"Grade": "float32"})
    gpa = gradePointAverage(s1, "Grade", "Credits")
    return s1

def plotGPA(gpagroup):
    import plotly.express as px
    import pandas as pd
    df = pd.DataFrame(dict(
        r= gpagroup, 
        theta=['Thai Language','Mathematics','Science and Technology',
               'Social Studies, Religion and Culture',
               'Health and Physical Education','Arts',
               'Occupations', 'Foreign Languages']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.show()
    
def formatGPA(gpa):
    decPoint, nDigit = str(gpa).split('.')
    lenDigit = len(nDigit)
    if lenDigit == 1:
        nDigit = nDigit + '0'
    return decPoint + '.' + nDigit[:2]

def getGPA(dataframe, studentID):
    qureytxt = 'StudentID == ' + str(studentID)
    s1 = dataframe.query(qureytxt)
    s1 = s1.astype({'Grade':'float32'})
    gpa = gradePointAverage(s1,'Grade', 'Credits')
    return gpa

def getYearGPA(dataframe, studentID):
    qureytxt = 'StudentID == ' + str(studentID)
    s1 = dataframe.query(qureytxt)
    s1 = s1.astype({'Grade':'float32'})
    years = set(s1["AcademicYear"])
    for year in years:
        s2 = s1.groupby(["AcademicYear"]).get_group(year)
        gpa = gradePointAverage(s2,'Grade', 'Credits')
        print(f'Year {year} your gpa is {formatGPA(gpa)}')
#    grouped = s1.groupby(["AcademicYear", "Semester"])

def getGPAAS(dataframe, id_student, subj):
    qtext = (
        "StudentID == "
        + str(id_student)
        + " and "        
        + "CourseID.str.contains('[" + subj + "]\d\d[1]\d\d')"
    )
    s1 = dataframe.query(qtext)
    s1 = s1.astype({"Grade": "float32"})
    gpa = gradePointAverage(s1, "Grade", "Credits")
    return formatGPA(gpa)

def getGGPAT(dataframe, id_student, subj, stype):
    # basic course 1 additional course 2 all 3
    typeSelect = ''
    match stype:
        case 1:
            typeSelect = '[1]'
        case 2:
            typeSelect = '[2]'
        case 3:
            typeSelect = '\d'
    qtext = (
        "StudentID == "
        + str(id_student)
        + " and "        
        + "CourseID.str.contains('[" + subj + "]\d\d" + typeSelect + "\d\d')"
    )
    s1 = dataframe.query(qtext)
    s1 = s1.astype({"Grade": "float32"})
    gpa = gradePointAverage(s1, "Grade", "Credits")
    return formatGPA(gpa)

def getGPAS(dataframe, id_student, year, term, subj):
    qtext = (
        "StudentID == "
        + str(id_student)
        + " and "
        + "AcademicYear == "
        + str(year)
        + " and "
        + "Semester == "
        + str(term)
        + " and "
        + "CourseID.str.contains('[" + subj + "]\d\d[1]\d\d')"
    )
    
    s1 = dataframe.query(qtext)
    s1 = s1.astype({"Grade": "float32"})
    gpa = gradePointAverage(s1, "Grade", "Credits")
    return formatGPA(gpa)

def getCNGPAS(dataframe, id_student):
    s1 = dataframe[dataframe['รหัสนักเรียน'] == id_student]
    firstname = s1['ชื่อ'].values[0]
    lastname = s1['นามสกุล'].values[0]
    sname = firstname + '  ' + lastname
    gpa = s1['GPAX'].values[0]
    s_info = [sname, formatGPA(gpa)]
    return s_info

def getCRUPAS(dataframe, id_student):
    s1 = dataframe[dataframe['รหัสนักเรียน'] == id_student]
    firstname = s1['ชื่อ'].values[0]
    lastname = s1['นามสกุล'].values[0]
    sname = [firstname, lastname]
    gpa = s1['GPAX'].values[0]
    #GPA SCI
    #GPA MAT

    s_info = [sname, formatGPA(gpa)]
    return s_info

def getCN(dataframe, gpaDF, id_student):
    file_output = f"filled_form{id_student}.pdf"
    #year 1/2564 2565 2666
    years = [2565, 2566, 2567]
    subj = [0, 0, 'ค', 'ว', 0, 0, 0, 0, 'อ']
    groups = [2, 3, 8]
    terms = [1, 2]
    qtext = (
        "StudentID == "
        + str(id_student)    
    )
    cnsGPA = getCNGPAS(gpaDF, id_student)    
    s1 = dataframe.query(qtext)
    sname = set(s1['Name'])
    print(*sname)
    lcn_gpas = []
    for groupSubject in groups:
        print(f"Subject : {nLearningGroup[groupSubject]}")
        for year in years:
            for term in terms:
                if year == 2567 and term == 2:
                    break
                else:
                    print(f"Academic Year = {year} Semester = {term} GPA = {getGPAS(dataframe, id_student, year, term, subj[groupSubject])}" )
                    lcn_gpas.append(getGPAS(dataframe, id_student, year, term, subj[groupSubject]))
        
        print("")
        print(f"GPAX {getGPAAS(dataframe, id_student, subj[groupSubject])}")
        lcn_gpas.append(getGPAAS(dataframe, id_student, subj[groupSubject]))
        print("----------------------------------------------")
    print(*lcn_gpas)
    text_positions[4][0] = cnsGPA[0]
    text_positions[5][0] = str(id_student)
    text_positions[7][0] = cnsGPA[1]
    text_positions[8][0] = str(lcn_gpas[6])
    text_positions[9][0] = str(lcn_gpas[7])
    text_positions[10][0] = str(lcn_gpas[8])
    text_positions[11][0] = str(lcn_gpas[9])
    text_positions[12][0] = str(lcn_gpas[10])
    text_positions[13][0] = str(lcn_gpas[11])
    text_positions[14][0] = str(lcn_gpas[0])
    text_positions[15][0] = str(lcn_gpas[1])
    text_positions[16][0] = str(lcn_gpas[2])
    text_positions[17][0] = str(lcn_gpas[3])
    text_positions[18][0] = str(lcn_gpas[4])
    text_positions[19][0] = str(lcn_gpas[5])
    text_positions[20][0] = str(lcn_gpas[12])
    text_positions[21][0] = str(lcn_gpas[13])
    text_positions[22][0] = str(lcn_gpas[14])
    text_positions[23][0] = str(lcn_gpas[15])
    text_positions[24][0] = str(lcn_gpas[16])
    text_positions[25][0] = str(lcn_gpas[17])
    
    fill_text_on_existing_pdf("form_template.pdf", file_output, text_positions, font_file="./THSarabunNew.ttf")            
    return 0

def getCNPDF(dataframelist, id_student):
    file_output = f"filled_form{id_student}.pdf"
    #year 1/2564 2565 2666
    years = [2566, 2567, 2568]
    subj = [0, 0, 'ค', 'ว', 0, 0, 0, 0, 'อ']
    groups = [2, 3, 8]
    terms = [1, 2]
    qtext = (
        "StudentID == "
        + str(id_student)    
    )
    dataframe, gpaDF = dataframelist
    cnsGPA = getCNGPAS(gpaDF, id_student)
    print(*cnsGPA)
    s1 = dataframe.query(qtext)
    sname = set(s1['Name'])
    print(*sname)
    lcn_gpas = []
    for groupSubject in groups:
        print(f"Subject : {nLearningGroup[groupSubject]}")
        for year in years:
            for term in terms:
                if year == 2568 and term == 2:
                    break
                else:
                    print(f"Academic Year = {year} Semester = {term} GPA = {getGPAS(dataframe, id_student, year, term, subj[groupSubject])}" )
                    lcn_gpas.append(getGPAS(dataframe, id_student, year, term, subj[groupSubject]))
        
        print("")
        print(f"GPAX {getGPAAS(dataframe, id_student, subj[groupSubject])}")
        lcn_gpas.append(getGPAAS(dataframe, id_student, subj[groupSubject]))
        print("----------------------------------------------")
    print(*lcn_gpas)
    text_positions[4][0] = cnsGPA[0]
    text_positions[5][0] = str(id_student)
    text_positions[7][0] = str(cnsGPA[1])
    text_positions[8][0] = str(lcn_gpas[6])
    text_positions[9][0] = str(lcn_gpas[7])
    text_positions[10][0] = str(lcn_gpas[8])
    text_positions[11][0] = str(lcn_gpas[9])
    text_positions[12][0] = str(lcn_gpas[10])
    text_positions[13][0] = str(lcn_gpas[11])
    text_positions[14][0] = str(lcn_gpas[0])
    text_positions[15][0] = str(lcn_gpas[1])
    text_positions[16][0] = str(lcn_gpas[2])
    text_positions[17][0] = str(lcn_gpas[3])
    text_positions[18][0] = str(lcn_gpas[4])
    text_positions[19][0] = str(lcn_gpas[5])
    text_positions[20][0] = str(lcn_gpas[12])
    text_positions[21][0] = str(lcn_gpas[13])
    text_positions[22][0] = str(lcn_gpas[14])
    text_positions[23][0] = str(lcn_gpas[15])
    text_positions[24][0] = str(lcn_gpas[16])
    text_positions[25][0] = str(lcn_gpas[17])
    
    fill_text_on_existing_pdf("cn69m4.pdf", file_output, text_positions, font_file="./THSarabunNew.ttf")            
    return 0

def getCRUSMTE(dataframelist, id_student):
    telnum = input('Telephone Number : ')
    file_output = f"D:\\download_t\\CRU_SMTEfilled_{id_student}.pdf"
    years = [2565, 2566, 2567]
    subj = [0, 0, 'ค', 'ว', 0, 0, 0, 0, 'อ']
    groups1 = [3, 2]
    type1 = [1, 1]
    groups2 = [3, 2, 8]
    type2 = [3, 3, 3]
    groups3 = [81, 82]
    type3 = [1,2]
    terms = [1, 2]
    qtext = (
        "StudentID == "
        + str(id_student)    
    )
    dataframe, gpaDF = dataframelist
    cruInfo = getCRUPAS(gpaDF, id_student)    
    s1 = dataframe.query(qtext)
    sname = set(s1['Name'])
    print(*sname)
    text_positions = make_cru1text_positions()
    school_record = []
    gpa_record = []
    print("============= SMTE =============")
    print("======== Basic Subject =========")
    for groupSubject in groups1:
        print(f"Subject : {nLearningGroup[groupSubject]}")
        for year in years:
            for term in terms:
                if year == 2567 and term == 2:
                    break
                else:
                    print(f"Academic Year = {year} Semester = {term}")
                    selectSubject = getDFAS(dataframe, id_student, year, term, subj[groupSubject], 1)
                    selectSubject = selectSubject.reset_index()
                    print("รหัสวิชา".center(8) + "ชื่อวิชา".center(30) + "หน่วยกิต".center(10) + "ผลการเรียน".center(10))
                    for index, row in selectSubject.iterrows():
                        print(str(row['CourseID']).ljust(8) + str(row['Title']).strip().ljust(30) + str(row['Credits']).center(5) + str(row['Grade']).rjust(6))
                        school_record.append([str(row['CourseID']), str(row['Credits']), str(row['Grade'])])
                    print("")
                    school_record.append("END_TERM")
        print(f"GPAX {getGGPAT(dataframe, id_student, subj[groupSubject], 1)}")
        gpa_record.append(f"{getGGPAT(dataframe, id_student, subj[groupSubject], 1)}")
        print(f"=============== {nLearningGroup[groupSubject]} type[1] ==================")
        print("")

    print(*school_record)
    print(*gpa_record)
    #insert school record to table
    start_position = 10
    position = start_position
    term_count = 0
    sr_number = 0
    while position < start_position + 60:
        if sr_number >= len(school_record):
             break
        print(position,sr_number, school_record[sr_number])
        if school_record[sr_number] == "END_TERM":
            if term_count == 1:
                position += 3            
            else:
                position = position                
            term_count = 0            
        else:
            text_positions[position][0] = school_record[sr_number][0]
            text_positions[position + 1][0] = school_record[sr_number][1]
            text_positions[position + 2][0] = school_record[sr_number][2]
            position += 3
            term_count += 1
        sr_number += 1        

    text_positions[0][0] = f"/เด็กหญิง {cruInfo[0][0]}"
    text_positions[1][0] = cruInfo[0][1]
    text_positions[2][0] = telnum
    text_positions[7][0] = cruInfo[1]
    text_positions[8][0] = gpa_record[0]
    text_positions[9][0] = gpa_record[1]
    text_positions[-4][0] = gpa_record[0]
    text_positions[-3][0] = gpa_record[1]

    fill_text_on_existing_pdf("CRU_SMTE_M4.pdf", file_output, text_positions, font_file="./THSarabunNew.ttf")
    return 0

def getCRUMEP2(dataframelist, id_student):
    telnum = input('Telephone Number : ')
    file_output = f"D:\\download_t\\CRU_MEP2filled_{id_student}.pdf"
    years = [2565, 2566, 2567]
    subj = [0, 0, 'ค', 'ว', 0, 0, 0, 0, 'อ']
    groups1 = [3, 2]
    type1 = [1, 1]
    groups2 = [3, 2, 8]
    type2 = [3, 3, 3]
    groups3 = [81, 82]
    type3 = [1,2]
    terms = [1, 2]
    qtext = (
        "StudentID == "
        + str(id_student)    
    )
    dataframe, gpaDF = dataframelist
    cruInfo = getCRUPAS(gpaDF, id_student)    
    s1 = dataframe.query(qtext)
    sname = set(s1['Name'])
    print(*sname)
    text_positions = make_cru3text_positions()
    school_record = []
    gpa_record = []
    print("============= Mini English Program (MEP) =============")
    print("=============== Foreign Languages ==================")
    for groupSubject in groups3:
        print(f"Subject : English Languages")
        for year in years:
            for term in terms:
                if year == 2567 and term == 2:
                    break
                else:
                    print(f"Academic Year = {year} Semester = {term}")
                    selectSubject = getDFAS(dataframe, id_student, year, term, subj[groupSubject//10], type3[groups3.index(groupSubject)])
                    
                    selectSubject = selectSubject.reset_index()
                    print("รหัสวิชา".center(8) + "ชื่อวิชา".center(30) + "หน่วยกิต".center(10) + "ผลการเรียน".center(10))
                    for index, row in selectSubject.iterrows():
                        print(str(row['CourseID']).ljust(8) + str(row['Title']).strip().ljust(30) + str(row['Credits']).strip().ljust(5) + str(row['Grade']).strip().rjust(6))
                        school_record.append([str(row['CourseID']), str(row['Credits']), str(row['Grade'])])
                    print("")
                    school_record.append("END_TERM")
        print(f"GPAX {getGGPAT(dataframe, id_student, subj[groupSubject//10], type3[groups3.index(groupSubject)])}")
        
        print(f"=============== {nLearningGroup[groupSubject//10]} type[{type3[groups3.index(groupSubject)]}] ==================")
        print("")    
    gpa_record.append(f"{getGGPAT(dataframe, id_student, subj[8], 3)}")
    print("----------------------------------------------")
    print(*school_record)
    print(*gpa_record)
    #insert school record to table
    start_position = 9
    position = start_position
    term_count = 0
    sr_number = 0
    while position < start_position + 60:
        if sr_number >= len(school_record):
             break
        print(position,sr_number, school_record[sr_number])
        if school_record[sr_number] == "END_TERM":
            if term_count == 1:
                position += 3            
            else:
                position = position                
            term_count = 0            
        else:
            text_positions[position][0] = school_record[sr_number][0]
            text_positions[position + 1][0] = school_record[sr_number][1]
            text_positions[position + 2][0] = school_record[sr_number][2]
            position += 3
            term_count += 1
        sr_number += 1        

    text_positions[0][0] = f"/เด็กหญิง {cruInfo[0][0]}"
    text_positions[1][0] = cruInfo[0][1]
    text_positions[2][0] = telnum
    text_positions[7][0] = cruInfo[1]
    text_positions[8][0] = gpa_record[0]        
    text_positions[-3][0] = gpa_record[0]
    fill_text_on_existing_pdf("CRU_MEP_ENGM4.pdf", file_output, text_positions, font_file="./THSarabunNew.ttf")
    return 0

def getCRUMEP1(dataframelist, id_student):
    telnum = input('Telephone Number : ')
    file_output = f"D:\\download_t\\CRU_MEP1filled_{id_student}.pdf"
    years = [2565, 2566, 2567]
    subj = [0, 0, 'ค', 'ว', 0, 0, 0, 0, 'อ']
    groups1 = [2, 3]
    type1 = [1, 1]
    groups2 = [3, 2, 8]
    type2 = [3, 3, 3]
    groups3 = [81, 82]
    type3 = [1,2]
    terms = [1, 2]
    qtext = (
        "StudentID == "
        + str(id_student)    
    )
    dataframe, gpaDF = dataframelist
    cruInfo = getCRUPAS(gpaDF, id_student)    
    s1 = dataframe.query(qtext)
    sname = set(s1['Name'])
    print(*sname)
    text_positions = make_cru2text_positions()
    school_record = []
    gpa_record = []
    print("============= Mini English Program (MEP) =============")
    print("=============== Science Mathematics ==================")
    for groupSubject in groups2:
        print(f"Subject : {nLearningGroup[groupSubject]}")
        for year in years:
            for term in terms:
                if year == 2567 and term == 2:
                    break
                else:
                    print(f"Academic Year = {year} Semester = {term}")
                    selectSubject = getDFAS(dataframe, id_student, year, term, subj[groupSubject], type2[groups2.index(groupSubject)])
                    
                    selectSubject = selectSubject.reset_index()
                    print("รหัสวิชา".center(8) + "ชื่อวิชา".center(30) + "หน่วยกิต".center(10) + "ผลการเรียน".center(10))
                    for index, row in selectSubject.iterrows():
                        print(str(row['CourseID']).ljust(8) + str(row['Title']).strip().ljust(30) + str(row['Credits']).strip().ljust(5) + str(row['Grade']).strip().rjust(6))
                        school_record.append([str(row['CourseID']), str(row['Credits']), str(row['Grade'])])
                    print("")
                    school_record.append("END_TERM")            
        #school_record.append("END_SUBJECT")
        print(f"GPAX {getGGPAT(dataframe, id_student, subj[groupSubject], type2[groups2.index(groupSubject)])}")
        gpa_record.append(f"{getGGPAT(dataframe, id_student, subj[groupSubject], type2[groups2.index(groupSubject)])}")
        print(f"=============== {nLearningGroup[groupSubject]} type[{type2[groups2.index(groupSubject)]}] ==================")
        print("")
    print(*school_record)
    #print(*gpa_record)
    #insert school record to table
    start_position = 11
    position = start_position
    term_count = 0
    sr_number = 0
    while position < start_position + 135:
        if sr_number >= len(school_record):
             break
        print(position,sr_number, school_record[sr_number])
        if school_record[sr_number] == "END_TERM":
            if term_count == 1:
                position += 6
            elif term_count == 2:
                position += 3
            else:
                position = position                
            term_count = 0            
        else:
            text_positions[position][0] = school_record[sr_number][0]
            text_positions[position + 1][0] = school_record[sr_number][1]
            text_positions[position + 2][0] = school_record[sr_number][2]
            position += 3
            term_count += 1
        sr_number += 1
        
#     for position in range(start_positon, start_positon + 135, 3):
#         if sr_number > len(school_record):
#             break
#         print(position,sr_number, school_record[sr_number])
#         if school_record[sr_number] != "END_TERM":       
#             text_positions[position][0] = school_record[sr_number][0]
#             text_positions[position + 1][0] = school_record[sr_number][1]
#             text_positions[position + 2][0] = school_record[sr_number][2]
#         elif school_record[sr_number] == "END_TERM":
#             position -= 3
#             sr_number += 1
#         sr_number += 1
    text_positions[0][0] = f"/เด็กหญิง {cruInfo[0][0]}"
    text_positions[1][0] = cruInfo[0][1]
    text_positions[2][0] = telnum
    text_positions[7][0] = cruInfo[1]
    text_positions[8][0] = gpa_record[0]
    text_positions[9][0] = gpa_record[1]
    text_positions[10][0] = gpa_record[2]   
    text_positions[146][0] = gpa_record[0]
    text_positions[147][0] = gpa_record[1]
    text_positions[148][0] = gpa_record[2]
    fill_text_on_existing_pdf("CRU_MEP_SMM4.pdf", file_output, text_positions, font_file="./THSarabunNew.ttf")
    return 0
    
def getCRU(dataframe, roomtype, id_student):
    #year 1/2564 2565 2666
    years = [2565, 2566, 2567]
    subj = [0, 0, 'ค', 'ว', 0, 0, 0, 0, 'อ']
    groups1 = [2, 3]
    type1 = [1, 1]
    groups2 = [2, 3, 8]
    type2 = [1, 1, 3]
    groups3 = [81, 82]
    type3 = [1,2]
    terms = [1, 2]
    qtext = (
        "StudentID == "
        + str(id_student)    
    )
    s1 = dataframe.query(qtext)
    sname = set(s1['Name'])
    print(*sname)
    match roomtype:
        case 1:
            print("============= SMTE =============")
            print("======== Basic Subject =========")
            for groupSubject in groups1:
                print(f"Subject : {nLearningGroup[groupSubject]}")
                for year in years:
                    for term in terms:
                        if year == 2567 and term == 2:
                            break
                        else:
                            print(f"Academic Year = {year} Semester = {term}")
                            selectSubject = getDFAS(dataframe, id_student, year, term, subj[groupSubject], 1)
                            selectSubject = selectSubject.reset_index()
                            print("รหัสวิชา".center(8) + "ชื่อวิชา".center(30) + "หน่วยกิต".center(10) + "ผลการเรียน".center(10))
                            for index, row in selectSubject.iterrows():
                                print(str(row['CourseID']).ljust(8) + str(row['Title']).strip().ljust(30) + str(row['Credits']).center(5) + str(row['Grade']).rjust(6))
                            print("")
                print(f"GPAX {getGGPAT(dataframe, id_student, subj[groupSubject], 1)}")
                print(f"=============== {nLearningGroup[groupSubject]} type[1] ==================")
                print("")
        case 2:
            print("============= Mini English Program (MEP) =============")
            print("=============== Science Mathematics ==================")
            for groupSubject in groups2:
                print(f"Subject : {nLearningGroup[groupSubject]}")
                for year in years:
                    for term in terms:
                        if year == 2566 and term == 2:
                            break
                        else:
                            print(f"Academic Year = {year} Semester = {term}")
                            selectSubject = getDFAS(dataframe, id_student, year, term, subj[groupSubject], type2[groups2.index(groupSubject)])
                            
                            selectSubject = selectSubject.reset_index()
                            print("รหัสวิชา".center(8) + "ชื่อวิชา".center(30) + "หน่วยกิต".center(10) + "ผลการเรียน".center(10))
                            for index, row in selectSubject.iterrows():
                                print(str(row['CourseID']).ljust(8) + str(row['Title']).strip().ljust(30) + str(row['Credits']).strip().ljust(5) + str(row['Grade']).strip().rjust(6))
                            print("")
                print(f"GPAX {getGGPAT(dataframe, id_student, subj[groupSubject], type2[groups2.index(groupSubject)])}")
                print(f"=============== {nLearningGroup[groupSubject]} type[{type2[groups2.index(groupSubject)]}] ==================")
                print("")
    #getDFAS
        case 3:
            print("============= Mini English Program (MEP) =============")
            print("=============== Foreign Languages ==================")
            for groupSubject in groups3:
                print(f"Subject : English Languages")
                for year in years:
                    for term in terms:
                        if year == 2566 and term == 2:
                            break
                        else:
                            print(f"Academic Year = {year} Semester = {term}")
                            selectSubject = getDFAS(dataframe, id_student, year, term, subj[groupSubject//10], type3[groups3.index(groupSubject)])
                            
                            selectSubject = selectSubject.reset_index()
                            print("รหัสวิชา".center(8) + "ชื่อวิชา".center(30) + "หน่วยกิต".center(10) + "ผลการเรียน".center(10))
                            for index, row in selectSubject.iterrows():
                                print(str(row['CourseID']).ljust(8) + str(row['Title']).strip().ljust(30) + str(row['Credits']).strip().ljust(5) + str(row['Grade']).strip().rjust(6))
                            print("")
                print(f"GPAX {getGGPAT(dataframe, id_student, subj[groupSubject//10], type3[groups3.index(groupSubject)])}")
                print(f"=============== {nLearningGroup[groupSubject//10]} type[{type3[groups3.index(groupSubject)]}] ==================")
                print("")
            
    
    print("----------------------------------------------")
    '''for groupSubject in groups:
        print(f"Subject : {nLearningGroup[groupSubject]}")
        for year in years:
            for term in terms:
                if year == 2566 and term == 2:
                    break
                else:
                    print(f"Academic Year = {year} Semester = {term} GPA = {getGPAS(dataframe, id_student, year, term, subj[groupSubject])}" )
        
        print("")
        print(f"GPAX {getGPAAS(dataframe, id_student, subj[groupSubject])}")
        print("----------------------------------------------")'''
                
    return 0

def getGPAX(dataframe, studentID):
    qureytxt = 'StudentID == ' + str(studentID)
    s1 = dataframe.query(qureytxt)
    s1 = s1.astype({'Grade':'float32'})    
    gpa = gradePointAverage(s1,'Grade', 'Credits')
    gpagroup = gradePerLearningAreas(s1)
    return gpa, gpagroup

def gradePointAverage(dataframe, Grade, Credits):
    gradeVal = dataframe[Grade]
    creditsWt = dataframe[Credits]
    return (gradeVal * creditsWt).sum() / creditsWt.sum()

def gradePerLearningAreas(dataframe):
    gpaGroup  = []
    print(f'Thai Language')
    c1 = dataframe['CourseID'].str.contains(".*ท.*")
    dataframeSelected = dataframe[(c1)]
    creditSum = dataframeSelected['Credits'].sum()
    gpa = gradePointAverage(dataframeSelected, 'Grade', 'Credits')
    gpaGroup.append(gpa)
    print(f'Sum all credits = {creditSum} GPA = {formatGPA(gpa)}')    
    
    print(f'Mathematics')
    c1 = dataframe['CourseID'].str.contains(".*ค.*")
    dataframeSelected = dataframe[(c1)]
    creditSum = dataframeSelected['Credits'].sum()
    gpa = gradePointAverage(dataframeSelected, 'Grade', 'Credits')
    gpaGroup.append(gpa)
    print(f'Sum all credits = {creditSum} GPA = {formatGPA(gpa)}')  
    
    print(f'Science and Technology')
    c1 = dataframe['CourseID'].str.contains(".*ว.*")
    dataframeSelected = dataframe[(c1)]
    creditSum = dataframeSelected['Credits'].sum()
    gpa = gradePointAverage(dataframeSelected, 'Grade', 'Credits')
    gpaGroup.append(gpa)
    print(f'Sum all credits = {creditSum} GPA = {formatGPA(gpa)}')      
    
    print(f'Social Studies, Religion and Culture')
    c1 = dataframe['CourseID'].str.contains(".*ส.*")
    dataframeSelected = dataframe[(c1)]
    creditSum = dataframeSelected['Credits'].sum()
    gpa = gradePointAverage(dataframeSelected, 'Grade', 'Credits')
    gpaGroup.append(gpa)
    print(f'Sum all credits = {creditSum} GPA = {formatGPA(gpa)}')      
    
    print(f'Health and Physical Education')
    c1 = dataframe['CourseID'].str.contains(".*พ.*")
    dataframeSelected = dataframe[(c1)]
    creditSum = dataframeSelected['Credits'].sum()
    gpa = gradePointAverage(dataframeSelected, 'Grade', 'Credits')
    gpaGroup.append(gpa)
    print(f'Sum all credits = {creditSum} GPA = {formatGPA(gpa)}')  
    
    print(f'Arts')
    c1 = dataframe['CourseID'].str.contains(".*ศ.*")
    dataframeSelected = dataframe[(c1)]
    creditSum = dataframeSelected['Credits'].sum()
    gpa = gradePointAverage(dataframeSelected, 'Grade', 'Credits')
    gpaGroup.append(gpa)
    print(f'Sum all credits = {creditSum} GPA = {formatGPA(gpa)}')
    
    print(f'Occupations')
    c1 = dataframe['CourseID'].str.contains(".*ง.*")
    dataframeSelected = dataframe[(c1)]
    creditSum = dataframeSelected['Credits'].sum()
    gpa = gradePointAverage(dataframeSelected, 'Grade', 'Credits')
    gpaGroup.append(gpa)
    print(f'Sum all credits = {creditSum} GPA = {formatGPA(gpa)}')
    
    print(f'Foreign Languages')
    c1 = dataframe['CourseID'].str.contains(".*อ.*")
    dataframeSelected = dataframe[(c1)]
    creditSum = dataframeSelected['Credits'].sum()
    gpa = gradePointAverage(dataframeSelected, 'Grade', 'Credits')
    gpaGroup.append(gpa)
    print(f'Sum all credits = {creditSum} GPA = {formatGPA(gpa)}')
    return gpaGroup
    
def gpatest(dataframe):
    from math import floor

    print(f'Thai Language')
    c1 = dataframe['CourseID'].str.contains(".*ท.*")
    dataframeSelected = dataframe[(c1)]
    creditSum = dataframeSelected['Credits'].sum()
    gpa = gradePointAverage(dataframeSelected, 'Grade', 'Credits')
    print(f'Sum all credits = {creditSum} GPA = {str(floor(gpa * 10**2) / 10**2)}')    
'''
                          Code
                      Thai	  English
Thai Language			ท		TH
Mathematics				ค		MA
Science and Technology	ว		SC
Social Studies			ส		SO
Health and PE			พ		HP
Arts					ศ		AR
Occupations				ง		OC
Foreign Languages		ต		FO
Korean					ก		KO
Chinese					จ		CH
Japanese				ญ		JA
French					ฝ		FR
Khmer 					ข		KH

qureytxt = 'StudentID == ' + str(42540) + 'and' + 'AcademicYear == ' + str(2564) + 'and' +'Semester == ' + str(1)
.query("CourseID.str.contains('[ว]\d\d[1]\d\d')")
'''