# Used to analyse the data-set
import pandas as pd
# To open an excel file but contain html code
dfm = pd.read_html('m3.xls', encoding = 'utf-8')
# change list to dataframe
df = dfm[0]
