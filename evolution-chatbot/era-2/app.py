import llama_cpp
from utils import cosine_similarity, to_numpy

# ฟังก์ชันโหลด Embedding Model
def get_embedding():
    return llama_cpp.Llama(
        model_path="./qwen3-embedding/Qwen3-Embedding-0.6B-Q8_0.gguf",
        embedding=True,
        verbose=False,
        pooling_type=3  # mean last pooling
    )

# Dictionary สำหรับเก็บ Intent กับ Response
intent_response_map = {
    "สวัสดี": "สวัสดีครับ/ค่ะ ฉันคือแชทบอทที่ถูกออกแบบมาเพื่อช่วยเหลือคุณ",
    "ทักทาย": "สวัสดีครับ/ค่ะ ฉันคือแชทบอทที่ถูกออกแบบมาเพื่อช่วยเหลือคุณ",
    "ซื้อของ": "สินค้าของเรามีดังต่อไปนี้: \n(ก-01) น้ำยาอเนกประสงค์ 1 ลิตร ราคา 100 บาท \n(ก-02) น้ำยาล้างจาน 500 มล. ราคา 50 บาท \n(ก-03) น้ำยาปรับผ้านุ่ม 1 ลิตร ราคา 120 บาท",
    "คุณชื่ออะไร": "ฉันไม่มีชื่อ แต่คุณสามารถเรียกฉันว่าแชทบอทได้",
    "คุณทำอะไรได้บ้าง": "ฉันสามารถตอบคำถามทั่วไปและช่วยเหลือคุณในเรื่องต่างๆ ได้",
    "ขอบคุณ": "ยินดีครับ/ค่ะ ถ้าคุณมีคำถามเพิ่มเติม อย่าลังเลที่จะถาม",
    "ลาก่อน": "ลาก่อนครับ/ค่ะ หวังว่าจะได้พูดคุยกันอีกครั้งในอนาคต",
    "ติดต่อเรา": "คุณสามารถติดต่อเราผ่านทางอีเมลหรือโทรศัพท์ที่ระบุไว้ในเว็บไซต์ของเรา"
}

# List ของ Intent ที่รองรับ
intent_list = [
    "สวัสดี",
    "ทักทาย",
    "ซื้อของ",
    "คุณชื่ออะไร",
    "คุณทำอะไรได้บ้าง",
    "ขอบคุณ",
    "ลาก่อน",
    "ติดต่อเรา"
]

# โหลด Model 1 ครั้ง
embedding_model = get_embedding()

# เก็บ Embedding ของ Intent ทั้งหมด
intent_embeddings = embedding_model.create_embedding(intent_list)
intent_embeddings = to_numpy(intent_embeddings)

# Interactive Application
max_round = 5
print("สวัสดี! ฉันเป็นแชทบอทที่จะช่วยคุณ กรุณาพิมพ์คำถามของคุณ")
for round in range(max_round):
    user_input = input("คุณ: ")
    user_input = user_input.strip()
    
    if user_input in intent_response_map:
        print(f"แชทบอท: {intent_response_map[user_input]}")
    else:
        # หา embedding ของ input
        user_emb = to_numpy(embedding_model.create_embedding(user_input))
        
        # คำนวณ cosine similarity
        scores = cosine_similarity(user_emb, intent_embeddings)
        
        # หา intent ที่มี similarity สูงสุด
        most_similar_intent_idx = scores.argmax()
        most_similar_intent = intent_list[most_similar_intent_idx]
        score = scores[most_similar_intent_idx]
        
        # ถ้า similarity > 0.2 ถือว่าเป็น intent นั้น
        if score > 0.2:
            print(f"แชทบอท: ฉันเข้าใจว่าคุณต้องการ {most_similar_intent} ({score:.2f}) \n\nAction: {intent_response_map[most_similar_intent]}\n-------------")
        else:
            print(f"แชทบอท: คำถามไม่อยู่ในฐานข้อมูลของฉัน (ความคล้ายคลึงที่สุด: {most_similar_intent} ({score:.2f}))\nกรุณาลองใหม่อีกครั้ง")