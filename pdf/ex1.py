import fitz  # PyMuPDF

def fill_text_in_pdf(input_pdf, output_pdf, text_positions, font_size=12, font_file="C:/Windows/Fonts/THSarabunNew.ttf"):
    """
    เติมข้อความลงใน PDF โดยใช้ฟอนต์จากไฟล์ .ttf
    :param input_pdf: ชื่อไฟล์ PDF ต้นฉบับ
    :param output_pdf: ชื่อไฟล์ PDF ที่จะบันทึกข้อความใหม่
    :param text_positions: ลิสต์ของข้อความและตำแหน่ง [(ข้อความ, (x, y))]
    :param font_size: ขนาดฟอนต์ (ค่าเริ่มต้น 14)
    :param font_file: เส้นทางไปยังไฟล์ฟอนต์ .ttf
    """
    doc = fitz.open(input_pdf)  # เปิดไฟล์ PDF
    page = doc[0]  # เลือกหน้าแรก (หรือระบุหน้า)
    
    # เพิ่มข้อความแต่ละตำแหน่ง
    for text, position in text_positions:
        page.insert_text(
            position,
            text,
            fontsize=font_size,
            fontfile=font_file,  # ใช้ฟอนต์จากไฟล์
            fill=(0, 0, 0)  # สีดำ
        )
    
    doc.save(output_pdf)  # บันทึกไฟล์ PDF ใหม่
    print(f"เติมข้อความสำเร็จ! บันทึกไว้ที่: {output_pdf}")

# ตัวอย่างตำแหน่งข้อความ (x, y) บน PDF
text_positions = [
    ("ภษา thai", (100, 550)),
    ("35 ปี", (100, 720)),
    ("1234567890123", (100, 690)),
    ("กรุงเทพมหานคร", (100, 660))
]

# เรียกใช้ฟังก์ชัน (ปรับเส้นทางไปยังไฟล์ฟอนต์ตามระบบของคุณ)
fill_text_in_pdf("form_template.pdf", "filled_form.pdf", text_positions, font_file="C:/Windows/Fonts/THSarabunNew.ttf")
