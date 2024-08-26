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
        {"type": "text", "text": "画像に写っている物のカテゴリーを抽出してください。なお、カテゴリーは4つに厳選し、キーワードの単語のみをjson形式で返してください。"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://storage.googleapis.com/flutterflow-io-6f20.appspot.com/teams/CHZs7LSoNO8ZEIbYf7UE/assets/27zj9i5d5anb/AMI.png",
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