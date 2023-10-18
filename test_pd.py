# Used to clean and analyse the data-set
import pandas as pd

datalist = ['m3.xls', 'm3-1.xls']
dflist = []

for data in datalist:
    # To open an excel file with encoding utf-8 for read thai
    dfm = pd.read_html(data, encoding = 'utf-8')
    # append data frame to dataframe list
    dflist.append(dfm[0])

all_student = pd.concat(dflist)

#convert data type
all_student.astype({'เลขประขำตัว':'str'}).dtypes

studentID = all_student.loc[all_student['เลขประขำตัว'] == 42540]

