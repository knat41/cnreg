# 
## การดึงข้อมูล 
เริ่มจากเมนู ข้อมูลสารสนเทศ
13. ประวัตินักเรียน


| รหัสโรงเรียน | ชั้น/ห้อง | เลขประจำตัวนักเรียน | คำนำหน้า  | ชื่อ        | นามสกุล      | เลขประจำตัวประชาชน   | วันเกิด      | เพศ  | สัญชาติ | ศาสนา | เชื้อชาติ | บิดา             | เลขประชาชนบิดา | มารดา                  | เลขประชาชนมารดา | ผู้ปกครอง | ระดับชั้น            | ปีที่เข้า | ภาคเรียนที่ | วันที่เข้า  | เข้าเรียนชั้น       | โรงเรียนเดิม    | จังหวัด | จบการศึกษาระดับ  |
|------------|---------|-----------------|----------|------------|------------|------------------|------------|-----|------|------|--------|----------------|--------------|----------------------|--------------|---------|-----------------|--------|--------|------------|-----------------|--------------|--------|---------------|
| 1020101003 | ม.3/x   | 4xx63           | เด็กหญิง | ชลกันยา | นุกูล   | 1-1002-0xxxx-83-0 | 19/04/25x3 | หญิง | ไทย   | พุทธ | ไทย     | นายชลบุรี เจริญฮวด |              | นางสาวกัลยา เจริญฮวด |               |         | มัธยมศึกษาตอนต้น | 2565   | 1      | 01/06/2565 | มัธยมศึกษาปีที่ 1 | อนุบาลชลบุรี  | ชลบุรี | ประถมศึกษาปีที่ 6 |

```python
การ load

```
	
## การตรวจสอบกิจกรรม
เริ่มจากเมนู 
```
ข้อมูลสารสนเทศ
ข้อมูล	11. ตรวจสอบการลงทะเบียน
ประเภทสาระวิชา	วิชากิจกรรม   	
ระดับชั้น ห้องที่	
ม.3 ทั้งหมด
```
## รหัสวิชากิจกรรมออกแบบไว้ดังนี้
m = ชั้นปีที่เรียน
* m = 1 ม. 1
* m = 2 ม. 2
* m = 3 ม. 3

A2m90x	แนะแนว
* x = 1 คือภาคเรียนที่ 1
* x = 2 คือภาคเรียนที่ 2

A2m90x	เนตรนารี
* x = 3 คือภาคเรียนที่ 1
* x = 4 คือภาคเรียนที่ 2

A2m90x	ยุวกาชาด
* x = 5 คือภาคเรียนที่ 1
* x = 6 คือภาคเรียนที่ 2

A2m90x	กิจกรรมเพื่อสังคมและสาธารณะประโยชน์
* x = 7 คือภาคเรียนที่ 1
* x = 8 คือภาคเรียนที่ 2

กิจกรรมชุมนุม
* A2m9x1	ชุมนุมภาษาไทย
* A2m9x2	ชุมนุมคณิตศาสตร์
* A2m9x3	ชุมนุมวิทยาศาสตร์และเทคโนโลยี
* A2m9x4	ชุมนุมสังคมศึกษา
* A2m9x5	ชุมนุมสุขศึกษาพลศึกษา
* A2m9x6	ชุมนุมศิลปศึกษา
* A2m9x7	ชุมนุมการงานอาชีพ
* A2m9x8	ชุมนุมภาษาต่างประเทศ
* A2m9x9	ชุมนุมส่งเสริมวิชาการ

กำหนดดังนี้
* x = 1 คือภาคเรียนที่ 1
* x = 2 คือภาคเรียนที่ 2
