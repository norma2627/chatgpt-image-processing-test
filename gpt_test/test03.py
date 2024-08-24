from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="chatgpt-4o-latest",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "「MBTI（マイヤーズ・ブリッグス・タイプ指標）という、16パターンから性格を診断するテストがあります。このテストは、以下の4つの次元で個人の傾向を評価します： 外向性 (Extraversion, E) – 内向性 (Introversion, I)、感覚 (Sensing, S) – 直観 (Intuition, N)、思考 (Thinking, T) – 感情 (Feeling, F)、判断 (Judging, J) – 知覚 (Perceiving, P)、これらの組み合わせによって、16種類の異なる性格タイプが定義されています。画像を見て、この画像を上げている人がどのタイプに当てはまるか予想してください。"},
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