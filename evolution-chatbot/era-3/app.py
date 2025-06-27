from openai import OpenAI

openai_client = OpenAI()

def get_chat_response(messages):
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

with open("knowledge.txt", "r", encoding="utf-8") as file:
    knowledge_base = file.read().strip()

messages = [
    {"role": "system", "content": f"""คุณเป็นแชทบอทที่ช่วยตอบคำถามและให้ข้อมูลต่างๆ ในภาษาไทย.
     --------------
     ข้อมูลมีดังต่อไปนี้:
     {knowledge_base}
     --------------
     """},
]


max_round = 5
print("สวัสดี! ฉันเป็นแชทบอทที่จะช่วยคุณ กรุณาพิมพ์คำถามของคุณ")
for round in range(max_round):
    user_input = input("คุณ: ")
    user_input = user_input.strip()
    prompt = user_input
    messages.append({"role": "user", "content": prompt})
    response = get_chat_response(messages)
    print(f"แชทบอท: {response}")
    messages.append({"role": "assistant", "content": response})
    print("-------------")