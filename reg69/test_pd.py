# CERT 
import pandas as pd

from cn_var import *

dflist = []
path = 'data'
print("Do you want to create new data on disk OR load old file ? (Create (C) / Load(L))")
answer = input(" : ")
if answer.upper() == 'C' or answer.upper() == 'CREATE':
    all_student = prePareData(path)
    m3_student = getData2Frame(all_student)
    print("Do you want to save data to disk ? (Yes(y) / No(n))")
    answer = input(" : ")
    if answer.upper() == 'Y' or answer.upper() == 'YES':
        #all_student.to_json('all66_m3.zip', orient = 'table', index = False, compression={'method': 'zip', 'compresslevel': 1})
        all_student.to_parquet("all68_m3.parquet", engine="fastparquet")
        m3_student.to_parquet("68_m3.parquet", engine="fastparquet")
    else:
        pass
else:
     #m3_student = pd.read_json('export66_m3.json', orient = 'table', compression={'method': 'zip', 'compresslevel': 1})
     #gpa_m3 = pd.read_json('gpa67_m3.zip', orient = 'table', compression={'method': 'zip', 'compresslevel': 1})
     m3_student = pd.read_parquet("68_m3.parquet", engine="fastparquet")
     gpa_m3 = pd.read_parquet("gpa68_m3.parquet", engine="fastparquet")

#rgpa68_m3 = load_student_profiles()
m3 = [m3_student, gpa_m3]
reqlist = [44132, 44149, 44150, 44151, 44188, 44220, 44220, 44228, 44230, 44233, 44239, 44260, 44263, 44274, 44364, 44380, 44404, 44416, 44435, 44439, 44464, 44465, 44477, 44485, 44504, 44555, 44556, 44564, 44566, 44572, 44574, 44626, 44642, 44648, 44649, 44658, 44666, 44680, 44686, 44688, 44712, 44751, 44495, 44176, 44603, 44736, 44558, 44431, 44311, 44124, 44394, 44224, 44623, 44168, 44193, 44473, 44217, 44391, 44429, 44125, 44679, 44290, 44138, 44185, 44432, 44513, 44376, 44457, 44373, 44171]
for idnumber in reqlist:
    getCNPDF(m3, idnumber)
#getCNPDF(m3, 44131)
#getCRUMEP1(m3, 44002)
#convert data type
# all_student.astype({'เลขประขำตัว':'str'}).dtypes
# 
# print("Do you want to save data to disk ? (Yes(y) / No(n))")
# answer = input(" : ")
# if answer.upper() == 'Y' or answer.upper() == 'YES':
#     m3_student.to_json('export66_m3.json', orient = 'table', index = False, compression={'method': 'zip', 'compresslevel': 1})
# else:
#     pass

# studentID = all_student.loc[all_student['เลขประขำตัว'] == 42540]
# 
# carryCourse = studentID.loc[studentID['รหัสวิชา'].str.contains(".*ว.*")]
'''
m3_all
how to save to excel
Create, write to and save a workbook:
carryCourse.to_excel("output.xlsx")

To specify the sheet name:
df1.to_excel("output.xlsx",
             sheet_name='Sheet_name_1')

If you wish to write to more than one sheet in the workbook,
it is necessary to specify an ExcelWriter object:
with pd.ExcelWriter('output.xlsx') as writer:  
    df1.to_excel(writer, sheet_name='Sheet_name_1')
    df2.to_excel(writer, sheet_name='Sheet_name_2')

dfm = pd.read_html('GPA2567_1_m3.xls', encoding = 'utf-8')
m3_data = pd.concat(dfm, ignore_index=True)
m3_data.to_json('gpa67_m3.zip', orient = 'table', index = False, compression={'method': 'zip', 'compresslevel': 1})
'''