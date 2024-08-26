# ChatGPT APIを使用し画像の物からカテゴリーのキーワードを2つ抽出する

from openai import OpenAI
import json

client = OpenAI()

response = client.chat.completions.create(
  model="chatgpt-4o-latest",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "画像に写っている物をできるだけ詳細なカテゴリに分類してください。カテゴリは最低でも10種類とし、それぞれのカテゴリは可能な限り具体的なものであるようにしてください。"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://storage.googleapis.com/flutterflow-io-6f20.appspot.com/teams/CHZs7LSoNO8ZEIbYf7UE/assets/45ng9xnxx7tv/UT.png",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

'''
keywords = response.choices[0].message.content.strip("```json")

with open('user1.json', 'w') as f:
    json.dump(keywords, f, ensure_ascii=False, indent=2)
'''

# debug用
print(response.choices[0])