import sys
import os

# กำหนด path ให้ mod_wsgi หาโปรเจกต์ได้
sys.path.insert(0, "/home/nat/ecnacadoc_app")

# กำหนด Environment ให้ใช้ Virtual Environment
activate_this = "/home/nat/ecnacadoc_app/venv00/bin/activate_this.py"
with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))

# Import Flask app
from app import app as application

