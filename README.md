# cnreg
python code for manipulation student data
# บันทึกเชิงเทคนิค สำหรับการตรวจสอบผลการเรียน
## สำหรับครู


### ตรวจอะไรบ้าง 
1. คะแนน และผลการเรียน
   - คะแนนที่ครูกรอกมี 4 ช่อง คือ ก่อนกลางภาค	กลางภาค	หลังกลางภาค	ปลายภาค
   - กรอกครบทุกช่อง ห้ามเว้นว่าง (ในกรณีสอบปลายภาค สามารถใส่ 0.0 ได้) 
   - คะแนนเก็บก่อนกลางภาค คะแนนสอบกลางภาค ควรมีอย่างน้อย 50 %
   - คะแนนที่ระบบ SGS ทำให้ ให้ตรวจ 2 ช่อง คือ รวม และผลการเรียน
   - คะแนนที่ระบบ SGS เตรียมสำหรับให้ตรวจสอบ เต็มก่อนกลางภาค	เต็มกลางภาค	เต็มหลังกลางภาค	เต็มปลายภาค	เต็มรวม
     - เต็มก่อนกลางภาค (คูณ 0.5 <= ก่อนกลางภาค)
     - เต็มกลางภาค (คูณ 0.5 <= กลางภาค)
2. คุณลักษณะอันพึงประสงค์
   - ช่องที่เกี่ยวข้อง คือ Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9 Q10 QGrade
   - มี 8 ข้อ ห้ามเว้นว่าง
   - ห้ามกรอกเกินไป 10 ข้อ
4. อ่าน คิดวิเคราะห์และเขียน
   - ช่องที่เกี่ยวข้อง คือ L1 L2 L3 L4 L5 LGrade
   - มี 5 ข้อ ห้ามเว้นว่าง
   - ถ้าครูจะกรอกให้คะแนนต่ำต้อง สัมพันธ์กับเกรด เช่น เกรด 1 อาจกรอก 1 ได้

### ไม่ตรวจ แต่ควรดู
1. ข้อมูลพื้นฐานรายวิชา ประกอบด้วย
   - รหัสวิชา
   - ชื่อวิชา
   - หน่วยกิต
2. ครูผู้สอน
3. ข้อมูลนักเรียน
   - เลขประขำตัว
   - ชื่อ-นามสกุล
   - เลขที่
4. ปีการศึกษา
5. ภาคเรียนที่

### รายการควรทำ
1. เกรดรวม
   - เกรดรวมเฉพาะวิชา
2. หน่วยกิตเฉพาะวิชา
   - หน่วยกิตรวม
3. การติด 0 ร มส
   
### รายการน่าทำ 
- ระบุช่องและจำนวนช่องคะแนนที่ขาดการกรอก
- เปรียบเทียบการกระจายคะแนนในแต่ละวิชาในห้องเรียน เช่น ในห้องคะแนนส่วนใหญ่อยู่ที่เท่าไร คะแนนที่โดดออกมาอยู่ที่เท่าไร
- เปรียบเทียบค่าเฉลี่ยแต่ละห้องให้1วิชา เช่น ภาษาไทย เอาค่าเฉลี่ยคะแนนภาษาไทยแต่ละห้องมาเทียบกันอาจจะพบว่าห้องที่เรียนกับครุคนเดียวกันมีคะแนนต่ำกว่าเรียนกับครูคนอื่น หรือ ครูปล่อยเกรดเป็นต้น
- ตรวจเช็คช่องคะแนนที่มีโอกาสกรอกผิด
  
__data frame__

| Command | Description |
| --- | --- |
| .head() | เพื่อดูข้อมูลส่วนหัว |
| git diff | Show file differences that haven't been staged |

การรวม data frame
concat() function

อ้างอิง [LINK Pages](https://pandas.pydata.org/docs/user_guide/merging.html)

### สถิติ 
p https://www.geo.fu-berlin.de/en/v/soga-py/Basics-of-statistics/Descriptive-Statistics/Measures-of-Position/Percentiles-and-Percentile-Rank/index.html


เปลี่ยนแปลงชื่อ
all_student.rename(columns={'เลขประขำตัว':'StudentID'},inplace=True)
all_student.rename(columns={'รหัสวิชา':'CourseID'},inplace=True)
all_student.rename(columns={'ชื่อวิชา':'Title'},inplace=True)
all_student.rename(columns={'หน่วยกิต':'Credits'},inplace=True)
all_student.rename(columns={'ผลการเรียน':'Grade'},inplace=True)
all_student.rename(columns={'กลุ่มที่':'SectionCourseID'},inplace=True)
all_student.rename(columns={'ปีการศึกษา':'AcademicYear'},inplace=True)
{'รหัสวิชา':'CourseID', 'ชื่อวิชา':'Title', 'หน่วยกิต':'Credits', 'กลุ่มที่':'SectionCourseID', 'ปีการศึกษา':'AcademicYear',
'ภาคเรียนที่':'Semester', 'ครูผู้สอน':'Instructor', 'ชื่อ-นามสกุล':'Name', 'ชั้น/ห้อง':'Classroom', 'เลขที่':'ClassNumber', 'กลางภาค':'MidtermExam','ปลายภาค':'FinalExam',
'หลังกลางภาค':'FinalFormative','ก่อนกลางภาค':'MidtermFormative', 'รวม':'TotalScore', 'รวมร้อยละ':'PercentScore', 'ผลการเรียน':'Grade', 'เต็มรวม':'FullMarks',
'เต็มก่อนกลางภาค':'MidForFullMarks', 'เต็มหลังกลางภาค':'FinForFullMarks', 'เต็มกลางภาค':'MidFullMarks', 'เต็มปลายภาค':'FinFullMarks'}

การเลือก

อ้างอิง [LINK Pages](https://blog.datath.com/cheatsheet-pandas/#withi_chekh_Summary_khxng_taela_khxlamn_count_min_max_mean)
https://medium.com/data-cafe-thailand/pandas-part-ii-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%A5%E0%B8%B7%E0%B8%AD%E0%B8%81-rows-columns-%E0%B9%81%E0%B8%A5%E0%B8%B0-row-filtering-%E0%B9%83%E0%B8%99-pandas-f2e6c9ca51e5

__os dir__
Use Glob Module to Search by Regular Expressions
import glob
glob.glob("/sys/*.log")

__เลือกยังไง__

อ้างอิง [LINK Pages](https://medium.com/@akaivdo/how-to-select-rows-containing-specified-string-7cbba8ffcac4)


เขียนยังไง หาได้ที่ [GitHub Pages](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
