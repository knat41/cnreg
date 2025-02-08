from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def fill_text_on_existing_pdf(input_pdf, output_pdf, text_positions, font_file="THSarabunNew.ttf", font_size=14):
    """
    เติมข้อความลงบน PDF เดิม (form_template.pdf) และบันทึกเป็น PDF ใหม่
    :param input_pdf: ไฟล์ PDF ต้นฉบับ
    :param output_pdf: ไฟล์ PDF ที่จะบันทึกข้อความใหม่
    :param text_positions: ลิสต์ของข้อความและตำแหน่ง [(ข้อความ, (x, y))]
    :param font_file: เส้นทางไปยังไฟล์ฟอนต์ .ttf
    :param font_size: ขนาดฟอนต์ (ค่าเริ่มต้น 14)
    """
    # สร้าง PDF ชั่วคราวเพื่อวางข้อความ
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    pdfmetrics.registerFont(TTFont("THSarabun", font_file))
    can.setFont("THSarabun", font_size)
    
    # เติมข้อความในแต่ละตำแหน่ง
    for text, position in text_positions:
        can.drawString(position[0], position[1], text)
    
    can.save()
    packet.seek(0)

    # รวม PDF เดิมกับ PDF ที่มีข้อความใหม่
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    overlay_pdf = PdfReader(packet)

    for page_number in range(len(reader.pages)):
        page = reader.pages[page_number]
        if page_number == 0:  # วางข้อความเฉพาะหน้าแรก
            page.merge_page(overlay_pdf.pages[0])
        writer.add_page(page)
    
    # บันทึกเป็นไฟล์ใหม่
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    
    print(f"เติมข้อความสำเร็จ! บันทึกไว้ที่: {output_pdf}")

# ตัวอย่างตำแหน่งข้อความ (x, y) บน PDF
text_positions = [
    ("ชลกันยานุกูล", (135, 661)),
    ("บางปลาสร้อย", (400, 661)),
    ("เมืองชลบุรี", (135, 634)),
    ("กรุงเทพมหานคร", (400, 634))
]

# เรียกใช้ฟังก์ชัน
fill_text_on_existing_pdf("form_template.pdf", "filled_form.pdf", text_positions, font_file="./THSarabunNew.ttf")
