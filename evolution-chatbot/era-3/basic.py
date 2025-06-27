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
    
prompt = "What is the capital of France?"
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
response = get_chat_response()
print(f"Prompt: {prompt}")
print(f"Response: {response}")