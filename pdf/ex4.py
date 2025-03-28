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
    ("ชลกันยานุกูล", (135, 661)), # ชื่อโรงเรียน
    ("บางปลาสร้อย", (400, 661)), #
    ("เมืองชลบุรี", (135, 634)),   #
    ("ชลบุรี", (400, 634)),
    ("นางฟ้า บนดอกบัวบาน", (330, 608)), # ชื่อ - นามสกุล
    ("44444", (160, 580)), # รหัสประจำตัวนักเรียน
    ("มัธยมศึกษาปีที่ 3", (330, 580)), 
    ("4.00", (415, 526)), # เกรดเฉลี่ยสะสม (gpax)
    ("4.00", (239, 410)), # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.1 เทอม 1)
    ("4.00", (296, 410)), # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.1 เทอม 2)
    ("4.00", (353, 410)), # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.2 เทอม 1)
    ("4.00", (409, 410)), # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.2 เทอม 2)
    ("4.00", (466, 410)), # เกรดเฉลี่ย สาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี (ม.3 เทอม 1)
    ("4.00", (526, 410)), # เกรดเฉลี่ย กลุ่มสาระพื้นฐานวิทยาศาสตร์และเทคโนโลยี รวม 5 ภาค
    ("4.00", (239, 374)), # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ (ม.1 เทอม 1)
    ("4.00", (296, 374)), # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ (ม.1 เทอม 2)
    ("4.00", (353, 374)), # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ (ม.2 เทอม 1)
    ("4.00", (409, 374)), # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ (ม.2 เทอม 2)
    ("4.00", (466, 374)), # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ (ม.3 เทอม 1)
    ("4.00", (526, 374)), # เกรดเฉลี่ย สาระพื้นฐานคณิตศาสตร์ รวม 5 ภาค
    ("4.00", (239, 338)), # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ (ม.1 เทอม 1)
    ("4.00", (296, 338)), # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ (ม.1 เทอม 2)
    ("4.00", (353, 338)), # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ (ม.2 เทอม 1)
    ("4.00", (409, 338)), # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ (ม.2 เทอม 2)
    ("4.00", (466, 338)), # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ (ม.3 เทอม 1)
    ("4.00", (526, 338)), # เกรดเฉลี่ย สาระพื้นฐานภาษาอังกฤษ รวม 5 ภาค
    ("นางสาววันวิสา ถุงทรัพย์", (115, 184)),
    ("นางนภาพร  มูลเมือง", (395, 220)),
    ("ผู้อำนวยการโรงเรียนชนกันยานุกูล", (384, 201))
]

# เรียกใช้ฟังก์ชัน
fill_text_on_existing_pdf("form_template.pdf", "filled_form.pdf", text_positions, font_file="./THSarabunNew.ttf")
