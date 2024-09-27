import os
import pandas as pd

from onet_var import *

print('Start create dataframe')
print('....')
data = 'D:\\pycode\\cn_reg\\onet67\\'  + '13.+ประวัตินักเรียน--2567_1-6-(1).xls'
print(f'Try to read file {data}')
dfm = pd.read_html(data, encoding = 'utf-8')
df = dfm[0]
df['nationality'] = df['สัญชาติ'].map(nationality_mapping)
df['sex'] = df['คำนำหน้า'].map(sex_mapping)
# ลบเครื่องหมาย '-' ออกจากคอลัมน์ 'เลขประจำตัวประชาชน'
df['id_number'] = df['เลขประจำตัวประชาชน'].str.replace('-', '')
# ใช้ฟังก์ชัน apply เพื่อสร้างคอลัมน์ types ใหม่
df['types'] = df.apply(determine_type, axis=1)
# กำหนดชื่อไฟล์
filename = 'onet67m6.xlsx'
# เลือกเฉพาะบางคอลัมน์ที่จะส่งออกไป Excel
columns_to_export = ['types', 'nationality', 'id_number',
                     'เลขประจำตัวนักเรียน', 'คำนำหน้า', 'ชื่อ', 'นามสกุล', 'sex']
# ตรวจสอบว่ามีไฟล์อยู่หรือไม่
if os.path.exists(filename):
    # ถ้ามีไฟล์แล้ว ให้ขอคำยืนยันว่าจะเขียนทับไหม
    confirm = input(f"ไฟล์ {filename} มีอยู่แล้ว คุณต้องการเขียนทับหรือไม่? (y/n): ").lower()
    
    if confirm == 'y':
        df[columns_to_export].to_excel(filename, index=False)
        print(f"เขียนทับไฟล์ {filename} เรียบร้อยแล้ว")
    else:
        print("ยกเลิกการเขียนไฟล์")
else:
    # ถ้าไม่มีไฟล์ ให้เขียนไฟล์ใหม่
    df[columns_to_export].to_excel(filename, index=False)
    print(f"บันทึกไฟล์ {filename} สำเร็จ")

'''
print(df['สัญชาติ'].value_counts())
# เลือกเฉพาะบางคอลัมน์ที่จะส่งออกไป Excel
columns_to_export = ['เลขประจำตัวประชาชน', 'ชื่อ']

# ส่งออกเฉพาะคอลัมน์ที่เลือกไปเป็นไฟล์ Excel
df[columns_to_export].to_excel('output.xlsx', index=False)
'''