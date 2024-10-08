# ChatGPT APIのテスト

画像から人を分析することは可能か？<br>
検証用に画像を5枚用意。(画像は[Unsplash](https://unsplash.com/)より)<br>
モデルは`gpt-4o`を選択。([モデル情報](https://platform.openai.com/docs/models))<br>


## 検証1: 画像＋性格
Code: `test01.py`<br>
Prompt: 性格を教えるように指示する。<br>

結果:<br>
```
音楽が好き:1枚目の画像に見られる大量のカセットテープやレコードから、この人は音楽が好きで、特に昔の音楽を大切にしていることがうかがえます。音楽への情熱を持っている人かもしれません。
整理整頓が得意: カセットテープやレコードが整然と並べられていることから、整理整頓が得意で綺 麗好きな性格が考えられます。
ミニマリズムとデザイン感覚:
他の画像に見られるシンプルで洗練されたインテリアやデザイン本などから、デザインやミニマリズムに興味があると思われます。アートやインテリアデザインに対するセンスがあるとも考えられます。
細部に気を配る:インテリアアイテムの 選び方や配置から、細部に気を配ることができる人であり、バランスや調和を大切に。
```
<br>

## 検証2: 画像＋性格イメージ
Code: `test02.py`<br>
Prompt: 性格を想像するように指示する。<br>

結果:<br>
```
この写真を上げた人は音楽やデザインに強い関心を持っている可能性があります。
以下のような性格を想像できます。
レトロ志向: カセットテープやレコードプレーヤーが見られます。過去の趣味 や文化に魅力を感じ、その感性を大切にしているようです。音楽を愛していて、特にクラシックロックやヴィンテージなサウンドを聞くのが好きそうな印象を受けます。
ミニマリスト: 部屋のインテリアはシンプル で、モノがきっちりと整理整頓されています。きれい好きで、物事を秩序立てることが好きな性格かもしれません。また、無駄を嫌い、必要なものだけを大切にする傾向があるかも。
デザインへの関心: 部屋に置か れたオブジェや本、シェルフに飾られたアイテムの選び方から、デザインに対する強い愛着が感じられます。自分の環境をおしゃれで洗練されたスタイルに整えることを楽しんでいる。
```
<br>

## 検証3: 画像＋MBTI
Code: `test03.py`<br>
Prompt: MBTIの説明をし、MBTIのどれにあてはまりそうか診断させる。<br>

結果:<br>
```
この画像は、レコードやカセットテープのコレクション、ミニマルなインテリアなどを含んでいることから、個々の要素に着目すると、次のようなMBTIのタイプが考えられるかもしれません。
INTJ または ISTJ: 知識や 情報を収集し整理する傾向が強い。レコードやカセットテープの整然としたコレクションは、このタイプの特性に合致するかもしれません。また、彼らは往々にしてミニマリスト的なデザインに魅力を感じることがあります。
INFJ または INFP: 創造的で、感覚的でありながらも整理された空間を好む傾向があります。インテリアの選定や配置が丁寧かつ美的なもので、自己表現を大切にすることが窺えます。
ISTP または ESTP: 実用性と美しさを重視し、物事を手に取り集めたりすることに興味があるタイプです。古いメディア形式に興味を引かれることがあり、そのコレクションも自身の生活に取り入れて楽しんでいる。
```
<br>