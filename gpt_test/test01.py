from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="chatgpt-4o-latest",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "この画像を上げた人の性格を教えてください。"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://images.unsplash.com/photo-1524779709304-40b5a3560c60?q=80&w=1076&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://images.unsplash.com/photo-1724004546024-7cb2bb22b5bb?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://images.unsplash.com/photo-1724004546082-edaf801e3129?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://images.unsplash.com/photo-1724004546303-c676b7d1ab71?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://images.unsplash.com/photo-1724004546109-2d68f5873500?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])