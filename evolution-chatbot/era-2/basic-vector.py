import llama_cpp
from utils import cosine_similarity, to_numpy

def get_embedding():
    return llama_cpp.Llama(model_path="./qwen3-embedding/Qwen3-Embedding-0.6B-Q8_0.gguf", 
                                #n_gpu_layers=-1,
                                embedding=True, 
                                verbose=False,
                                pooling_type=3) # 3 is mean last

embedding_model = get_embedding()
query = "ดีครับ<|endoftext|>" #หาของ<|endoftext|>

res = embedding_model.create_embedding(query) #หาของ<|endoftext|>
print(to_numpy(res))

intent_list = [
    "สวัสดี<|endoftext|>",
    "ซื้อของ<|endoftext|>",
    "คุณชื่ออะไร<|endoftext|>",
    "บอกลา<|endoftext|>",
    "ติดต่อเรา<|endoftext|>",
]

bulk_vectors = embedding_model.create_embedding(intent_list)

res = to_numpy(res)
bulk_vectors = to_numpy(bulk_vectors)

cosine_similarity_scores = cosine_similarity(res, bulk_vectors)

for intent, score in zip(intent_list, cosine_similarity_scores):
    print(f"Intent: {intent}, Cosine Similarity: {score:.4f}")
