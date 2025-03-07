'''
CN reg 2567
Programmer : NAT  KANJANASIRI

'''
import pandas as pd

from cnreg import *

file = 'studentdata67m3.xls'
df = pd.read_html(file, encoding = 'utf-8')
# selected first DataFrame because read_html output with list
df = df[0]  
df.rename(columns=column_mapping, inplace=True)
unique_values = df['previous_school'].unique()

df_school_counts = df['previous_school'].value_counts().reset_index()
df_school_counts.columns = ['previous_school', 'count']
print(df_school_counts)


'''
school_counts = df['previous_school'].value_counts()
'''