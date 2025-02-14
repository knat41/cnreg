import mariadb
import sys
from flask import Flask, render_template, request

app = Flask(__name__)

# ตั้งค่าการเชื่อมต่อ MariaDB
db_config = {
    "host": "localhost",
    "user": "admin",
    "password": "password123",
    "database": "e_academic"
}

try:
    conn = mariadb.connect(**db_config)
    cursor = conn.cursor()
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    sys.exit(1)

@app.route('/')
def index():
    return "ระบบ e-Academic Document พร้อมทำงาน"

@app.route('/add', methods=['POST'])
def add_request():
    student_name = request.form['student_name']
    document_type = request.form['document_type']
    
    cursor.execute("INSERT INTO requests (student_name, document_type, status) VALUES (?, ?, 'pending')",
                   (student_name, document_type))
    conn.commit()
    
    return "บันทึกคำร้องสำเร็จ!"

if __name__ == '__main__':
    app.run(debug=True)

