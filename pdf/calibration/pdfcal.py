from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

# === ตั้งค่าชื่อไฟล์ ===
input_pdf = "input.pdf"   # ไฟล์ PDF ต้นฉบับ
output_pdf = "output_with_grid.pdf"  # ไฟล์ PDF ที่มีตาราง

# === อ่านไฟล์ PDF เดิม ===
reader = PdfReader(input_pdf)
writer = PdfWriter()

# === ตั้งค่าตาราง ===
grid_size = 10  # ขนาดช่องตาราง (10 pt)

# === วาดตารางและตัวเลขกำกับแกน ===
for page_num in range(len(reader.pages)):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    
    width, height = letter

    # กำหนดสีเทาอ่อนสำหรับเส้นตาราง
    can.setStrokeColorRGB(0.7, 0.7, 0.7)  
    can.setFont("Helvetica", 6)  # กำหนดขนาดตัวอักษร

    # วาดเส้นแนวตั้ง + ตัวเลขแกน X
    for x in range(0, int(width), grid_size):
        can.line(x, 0, x, height)
        if x % 50 == 0:  # ใส่ตัวเลขทุกๆ 50 pt
            can.drawString(x + 2, height - 15, str(x))

    # วาดเส้นแนวนอน + ตัวเลขแกน Y
    for y in range(0, int(height), grid_size):
        can.line(0, y, width, y)
        if y % 50 == 0:  # ใส่ตัวเลขทุกๆ 50 pt
            can.drawString(5, y + 2, str(y))

    can.save()

    # === ซ้อนตารางลงใน PDF เดิม ===
    packet.seek(0)
    new_pdf = PdfReader(packet)
    page = reader.pages[page_num]
    page.merge_page(new_pdf.pages[0])  # ซ้อนตารางลงไป
    writer.add_page(page)

# === บันทึกไฟล์ PDF ใหม่ ===
with open(output_pdf, "wb") as output_file:
    writer.write(output_file)

print(f"✅ เพิ่มตารางและตัวเลขกำกับแกน X, Y เรียบร้อย! -> {output_pdf}")

