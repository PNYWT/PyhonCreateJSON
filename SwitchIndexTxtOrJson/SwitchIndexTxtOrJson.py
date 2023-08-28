import json

# อ่านข้อมูล JSON จากไฟล์ .txt

with open('data_bt.txt', 'r', encoding='utf-8') as file:
    json_text  = file.read()

# แปลงข้อความ JSON เป็นโครงสร้าง JSON
data = json.loads(json_text)

# สับเปลี่ยนตำแหน่งข้อมูลในรายการ "data"
swapped_data = data["data"][::-1]

# สร้างโครงสร้างใหม่ของข้อมูล JSON
new_data = {"data": swapped_data}

# แปลงโครงสร้าง JSON เป็นข้อความ JSON
new_json_text = json.dumps(new_data, indent=4)

# เขียนข้อมูล JSON กลับลงในไฟล์ .txt
# with open('output.txt', 'w') as file:
#     file.write(new_json_text)
with open('output.json', 'w') as file:
    file.write(new_json_text)