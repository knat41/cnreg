# Used to clean and analyse the data-set
import pandas as pd

from cn_var import *

datalist = ['m3.xls', 'm3-1.xls']
dflist = []
path = 'm3_all'
print("Do you want to create new data on disk OR load old file ? (Create (C) / Load(L))")
answer = input(" : ")
if answer.upper() == 'C' or answer.upper() == 'CREATE':
    all_student = prePareData(path)
    m3_student = getData2Frame(all_student)
    print("Do you want to save data to disk ? (Yes(y) / No(n))")
    answer = input(" : ")
    if answer.upper() == 'Y' or answer.upper() == 'YES':
        all_student.to_json('all66_m3.zip', orient = 'table', index = False, compression={'method': 'zip', 'compresslevel': 1})
    else:
        pass
else:
     m3_student = pd.read_json('export66_m3.json', orient = 'table', compression={'method': 'zip', 'compresslevel': 1})
#convert data type
all_student.astype({'เลขประขำตัว':'str'}).dtypes

print("Do you want to save data to disk ? (Yes(y) / No(n))")
answer = input(" : ")
if answer.upper() == 'Y' or answer.upper() == 'YES':
    m3_student.to_json('export66_m3.json', orient = 'table', index = False, compression={'method': 'zip', 'compresslevel': 1})
else:
    pass

studentID = all_student.loc[all_student['เลขประขำตัว'] == 42540]

carryCourse = studentID.loc[studentID['รหัสวิชา'].str.contains(".*ว.*")]
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
'''