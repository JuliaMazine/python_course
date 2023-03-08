from collections import Counter as cnt
import json
lines = list()
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for j in range(len(data['acts'])):
        for k in range(len(data['acts'][j]['scenes'])):
            for m in range(len(data['acts'][j]['scenes'][k]['action'])):
                    lines.extend(data['acts'][j]['scenes'][k]['action'][m]['says'])
word_list = [word for line in lines for word in line.split()]
c = cnt(word_list)
print(c.most_common(20), c.most_common()[-21::])


