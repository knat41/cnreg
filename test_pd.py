# Used to clean and analyse the data-set
import pandas as pd

from cn_var import *

datalist = ['m3.xls', 'm3-1.xls']
dflist = []

print('Start create dataframe')
print('....')

for data in datalist:
    # To open an excel file with encoding utf-8 for read thai
    dfm = pd.read_html(data, encoding = 'utf-8')
    # append data frame to dataframe list
    dflist.append(dfm[0])

all_student = pd.concat(dflist)

print('created done')

#convert data type
all_student.astype({'เลขประขำตัว':'str'}).dtypes

studentID = all_student.loc[all_student['เลขประขำตัว'] == 42540]

carryCourse = studentID.loc[studentID['รหัสวิชา'].str.contains(".*ว.*")]
'''
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
