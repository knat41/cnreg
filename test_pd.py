# Used to clean and analyse the data-set
import pandas as pd
# To open an excel file
dfm = pd.read_html('m3.xls', encoding = 'utf-8')
df = dfm[0]
