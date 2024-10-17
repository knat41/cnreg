# cnreg SGS
python code for manipulation SGS data
# บันทึก CS Log สำหรับการตรวจสอบการกรอกคะแนน
## สำหรับครู

```python
# ตรวจสอบว่ามี L1 - L5 ว่างบางส่วน
missing_some_L = s67[['L1', 'L2', 'L3', 'L4', 'L5']].isnull().any(axis=1)

# เลือกแถวที่ L1 - L5 ว่างบางส่วน และแสดง Title และ Instructor
missing_instructors_some_L = s67[missing_some_L][['Title', 'Instructor', 'L1', 'L2', 'L3', 'L4', 'L5']]

# แสดงข้อมูล
print(missing_instructors_some_L)
```
	
	
	