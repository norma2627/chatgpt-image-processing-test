import json

with open('user1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

words = data

print(words)
