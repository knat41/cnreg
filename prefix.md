def split_name_prefix(name):
    prefixes = ["นาย", "นาง", "นางสาว"]
    for prefix in prefixes:
        if name.startswith(prefix):
            return prefix, name[len(prefix):].strip()
    return "", name

# ตัวอย่างการใช้งาน
input_name = "นางสาวพรชนก"
prefix, remaining_name = split_name_prefix(input_name)

print("คำนำหน้า:", prefix)
print("ชื่อ:", remaining_name)

