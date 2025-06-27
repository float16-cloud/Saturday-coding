# เก็บ intent ที่ผู้ใช้พูดถึง
current_intents = []

# Dictionary ของคำถามและ intent
question_and_intent = {
    "สวัสดี": {"intent": [], "response": "สวัสดีครับ/ค่ะ ฉันคือแชทบอทที่ช่วยเหลือคุณ"},
    "ฉันปวดท้อง": {"intent": ["อาการ"], "response": "อาการปวดท้องอาจเกิดจากหลายสาเหตุครับ/ค่ะ"},
    "ฉันอยากนัดแพทย์": {"intent": ["นัดหมาย"], "response": "คุณสามารถนัดแพทย์ได้ผ่านแอปพลิเคชันของเราครับ/ค่ะ"},
    "อาการท้องเสีย": {"intent": ["อาการ", "ท้องเสีย"], "response": "ท้องเสียควรดื่มน้ำมาก ๆ และหลีกเลี่ยงอาหารที่ไม่สะอาด"},
    "ฉันไม่สบาย": {"intent": ["อาการ"], "response": "คุณมีอาการอย่างไรครับ/ค่ะ"},
    "ประเมินอาการ": {"intent": ["ประเมินอาการ"], "response": "โปรดแจ้งอาการที่คุณมีครับ/ค่ะ"}
}

# เงื่อนไขพิเศษเมื่อ intent ครบ
special_conditions = {
    frozenset(["อาการ", "ท้องเสีย", "นัดหมาย"]): "คุณสามารถนัดแพทย์เพื่อตรวจอาการท้องเสียได้แล้วครับ/ค่ะ"
}

# จำนวนรอบที่ต้องการรับข้อมูล
max_round = 5

for round_num in range(max_round):
    user_input = input("คุณ: ")
    user_input = user_input.strip().lower()

    matched = False

    for question, data in question_and_intent.items():
        if user_input == question.lower():
            response = data["response"]
            intent_list = data["intent"]
            for intent in intent_list:
                if intent not in current_intents:
                    current_intents.append(intent)
            print("แชทบอท:", response)
            matched = True
            break

    if not matched:
        print("แชทบอท: คำถามไม่อยู่ในฐานข้อมูลของฉัน กรุณาลองใหม่อีกครั้ง")

    # ตรวจสอบเงื่อนไขพิเศษเมื่อ intent ครบ
    intent_set = frozenset(current_intents)
    if intent_set in special_conditions:
        print("แชทบอท:", special_conditions[intent_set])
    print("แชทบอท: : หากคุณมีคำถามเร่งด่วนโปรดติดต่อ เบอร์ 1669 หรือ 1330 ครับ/ค่ะ")