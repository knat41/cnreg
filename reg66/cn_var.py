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

fpath = ''
m = [1, 2, 3, 4, 5, 6]

ldir = []

def prePareData(path):
    import pandas as pd
    import glob
    dflist = []    
    print('Start create dataframe')
    print('....')
    creadfile = 0
    fpath = '../' + path + '/*.xls'
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

def getCN(dataframe, id_student):
    #year 1/2564 2565 2666
    years = [2564, 2565, 2566]
    subj = [0, 0, 'ค', 'ว', 0, 0, 0, 0, 'อ']
    groups = [2, 3, 8]
    terms = [1, 2]
    qtext = (
        "StudentID == "
        + str(id_student)    
    )
    s1 = dataframe.query(qtext)
    sname = set(s1['Name'])
    print(*sname)
    for groupSubject in groups:
        print(f"Subject : {nLearningGroup[groupSubject]}")
        for year in years:
            for term in terms:
                if year == 2566 and term == 2:
                    break
                else:
                    print(f"Academic Year = {year} Semester = {term} GPA = {getGPAS(dataframe, id_student, year, term, subj[groupSubject])}" )
        
        print("")
        print(f"GPAX {getGPAAS(dataframe, id_student, subj[groupSubject])}")
        print("----------------------------------------------")
                
    return 0

def getCRU(dataframe, roomtype, id_student):
    #year 1/2564 2565 2666
    years = [2564, 2565, 2566]
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
                        if year == 2566 and term == 2:
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