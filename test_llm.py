import ollama

response = ollama.chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": "What is inventory management? Answer in one sentence."
        }
    ]
)

print(response["message"]["content"])
