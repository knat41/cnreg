# ตัวอย่างการวาดลง pdf
pip install PyPDF2
pip install reportlab

ตัวนี้ test ใช้ภาษาไทยไม่ได้
pip install PyMuPDF
## วิธีปรับตำแหน่ง
* เปิด PDF ต้นฉบับ (form_template.pdf) ด้วยโปรแกรมเช่น Adobe Acrobat หรือ Foxit PDF
* ใช้เครื่องมือวัดตำแหน่ง (Measurement Tool) เพื่อดูตำแหน่ง (x, y) ที่ต้องการใส่ข้อความ
* ปรับตำแหน่งในลิสต์ text_positions
## ตัวอย่างการปรับข้อความให้กึ่งกลางหรือขวา
วางข้อความกึ่งกลางหน้า:
