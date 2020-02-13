import xml.etree.ElementTree as ET
from pprint import pprint

tree = ET.parse('newsafr.xml')
root = tree.getroot()
items = root.findall('channel/item')
texts_list = []
words = []
num_list = []
for item in items:
    texts = item.find('description').text
    texts_list.append(texts)
for text in texts_list:
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