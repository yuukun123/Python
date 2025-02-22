import openai
import os

def chat_with_gpt(prompt):
    api_key = "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"  # Lấy API key từ biến môi trường
    if not api_key:
        raise ValueError("API Key chưa được thiết lập! Hãy đặt OPENAI_API_KEY.")

    client = openai.OpenAI(api_key=api_key)  # Truyền API key vào client
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Đổi từ "gpt-4" sang "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# Test API
user_input = "AI là gì?"
output = chat_with_gpt(user_input)
print(output)
