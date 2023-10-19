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

__data frame__

| Command | Description |
| --- | --- |
| .head() | เพื่อดูข้อมูลส่วนหัว |
| git diff | Show file differences that haven't been staged |

การรวม data frame
concat() function

อ้างอิง [LINK Pages](https://pandas.pydata.org/docs/user_guide/merging.html)



การเลือก

อ้างอิง [LINK Pages](https://blog.datath.com/cheatsheet-pandas/#withi_chekh_Summary_khxng_taela_khxlamn_count_min_max_mean)


__os dir__
Use Glob Module to Search by Regular Expressions
import glob
glob.glob("/sys/*.log")

__เลือกยังไง__

อ้างอิง [LINK Pages](https://medium.com/@akaivdo/how-to-select-rows-containing-specified-string-7cbba8ffcac4)


เขียนยังไง หาได้ที่ [GitHub Pages](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
