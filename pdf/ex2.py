from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

def fill_text_in_pdf(output_pdf, text_positions, font_file="THSarabunNew.ttf", font_size=14):
    """
    สร้าง PDF พร้อมเติมข้อความภาษาไทย
    :param output_pdf: ชื่อไฟล์ PDF ที่จะบันทึกข้อความใหม่
    :param text_positions: ลิสต์ของข้อความและตำแหน่ง [(ข้อความ, (x, y))]
    :param font_file: เส้นทางไปยังไฟล์ฟอนต์ .ttf (ต้องเป็นฟอนต์ที่รองรับภาษาไทย)
    :param font_size: ขนาดฟอนต์ (ค่าเริ่มต้น 14)
    """
    c = canvas.Canvas(output_pdf, pagesize=A4)  # สร้าง PDF ขนาด A4
    pdfmetrics.registerFont(TTFont("THSarabunNew", font_file))  # ลงทะเบียนฟอนต์
    c.setFont("THSarabunNew", font_size)  # ตั้งค่าฟอนต์และขนาด
    
    # เติมข้อความในแต่ละตำแหน่ง
    for text, position in text_positions:
        c.drawString(position[0], position[1], text)  # วางข้อความที่ (x, y)
    
    c.save()  # บันทึก PDF
    print(f"เติมข้อความสำเร็จ! บันทึกไว้ที่: {output_pdf}")

# ตัวอย่างตำแหน่งข้อความ (x, y) บน PDF
text_positions = [
    ("นายสมชาย ใจดี", (100, 750)),
    ("35 ปี", (100, 720)),
    ("1234567890123", (100, 690)),
    ("กรุงเทพมหานคร", (100, 660))
]

# เรียกใช้ฟังก์ชัน (ปรับเส้นทางฟอนต์ให้ถูกต้อง)
fill_text_in_pdf("filled_form.pdf", text_positions, font_file="./THSarabunNew.ttf")
