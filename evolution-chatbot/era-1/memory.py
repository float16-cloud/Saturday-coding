question_and_answer = {
    "สวัสดี": "สวัสดีครับ/ค่ะ ฉันคือแชทบอทที่ถูกออกแบบมาเพื่อช่วยเหลือคุณ",
    "คุณชื่ออะไร": "ฉันไม่มีชื่อ แต่คุณสามารถเรียกฉันว่าแชทบอทได้",
    "คุณทำอะไรได้บ้าง": "ฉันสามารถตอบคำถามทั่วไปและช่วยเหลือคุณในเรื่องต่างๆ ได้",
    "ขอบคุณ": "ยินดีครับ/ค่ะ ถ้าคุณมีคำถามเพิ่มเติม อย่าลังเลที่จะถาม",
    "ลาก่อน": "ลาก่อนครับ/ค่ะ หวังว่าจะได้พูดคุยกันอีกครั้งในอนาคต",
    "ซื้อของ": "สินค้าของเรามีดังต่อไปนี้ : \n(ก-01) น้ำยาอเนกประสงค์ 1 ลิตร ราคา 100 บาท \n(ก-02) น้ำยาล้างจาน 500 มล. ราคา 50 บาท \n(ก-03) น้ำยาปรับผ้านุ่ม 1 ลิตร ราคา 120 บาท",
    "ติดต่อเรา": "คุณสามารถติดต่อเราผ่านทางอีเมลหรือโทรศัพท์ที่ระบุไว้ในเว็บไซต์ของเรา",
    "ก-01": "น้ำยาอเนกประสงค์ 1 ลิตร ราคา 100 บาท",
    "ก-02": "น้ำยาล้างจาน 500 มล. ราคา 50 บาท",
    "ก-03": "น้ำยาปรับผ้านุ่ม 1 ลิตร ราคา 120 บาท",
}

should_remember = ["ก-01", "ก-02", "ก-03"]

# สร้าง dictionary สำหรับเก็บราคา
product_price = {
    "ก-01": 100,
    "ก-02": 50,
    "ก-03": 120
}

# สร้าง dictionary สำหรับเก็บรายการสินค้าที่สั่งซื้อ
order_items = {}

# สร้าง dictionary สำหรับเก็บจำนวนสินค้าที่สั่งไป
cart = {}

# ฟังก์ชันจัดการการเพิ่มสินค้า
def add_to_cart(product_code):
    if product_code in cart:
        cart[product_code] += 1
    else:
        cart[product_code] = 1
    print(f"เพิ่ม {question_and_answer[product_code]} จำนวน {cart[product_code]} ชิ้น")

# ฟังก์ชันแสดงรายการในตะกร้า
def show_cart():
    if not cart:
        print("ไม่มีรายการสินค้าในตะกร้า")
    else:
        print("รายการสินค้าในตะกร้า:")
        total = 0
        for item, qty in cart.items():
            print(f"{item}: {question_and_answer[item]} จำนวน {qty} ชิ้น - ราคารวม {qty * product_price[item]} บาท")
            total += qty * product_price[item]
        print(f"รวมทั้งหมด: {total} บาท")

# ฟังก์ชันสรุปรายการสั่งซื้อ
def checkout():
    if not cart:
        print("ไม่มีรายการสินค้าที่สั่งซื้อ")
    else:
        print("สรุปรายการสั่งซื้อ:")
        total = 0
        for item, qty in cart.items():
            print(f"{item}: {question_and_answer[item]} จำนวน {qty} ชิ้น - ราคารวม {qty * product_price[item]} บาท")
            total += qty * product_price[item]
        print(f"รวมทั้งหมด: {total} บาท")

# ฟังก์ชันหลัก
def chatbot():
    max_round = 5
    for _ in range(max_round):
        user_input = input("กรุณาพิมพ์คำถาม/คำสั่ง: ")
        user_input = user_input.strip()

        if user_input in question_and_answer:
            if user_input in should_remember:
                add_to_cart(user_input)
            else:
                print(question_and_answer[user_input])
        elif user_input == "คิดเงิน":
            checkout()
        else:
            print("คำถามไม่อยู่ในฐานข้อมูลของฉัน กรุณาลองใหม่อีกครั้ง")

# เรียกใช้ฟังก์ชัน
chatbot()