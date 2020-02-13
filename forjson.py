import json
from pprint import pprint

with open('newsafr.json', encoding='UTF-8') as f:
    data = json.load(f)

news_data = data['rss']['channel']['items']
texts = []
words = []
num_list = []
for item in news_data:
    description = item.get('description')
    texts.append(description)
for text in texts:
    t = text.split(' ')
    for word in t:
        if len(word) > 6:
            words.append(word)
for w in words:
    num = words.count(w)
    num_list.append(num)
num_dict = dict(zip(num_list, words))
top_nums = []
while len(top_nums) < 11:
    big = max(num_list)
    top_nums.append(big)
    num_list = list(filter(lambda a: a != big, num_list))
for num in top_nums:
    print(f'Слово "{num_dict.get(num)}" встречается {num} раз')