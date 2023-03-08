import json
from collections import defaultdict

dic = defaultdict(list)
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for j in range(len(data['acts'])):
        for k in range(len(data['acts'][j]['scenes'])):
            for l in range(len(data['acts'][j]['scenes'][k]['action'])):
                for q in data['acts'][j]['scenes'][k]['action'][l]['says']:
                    dic[data['acts'][j]['scenes'][k]['action'][l]['character']].append(q)

print(dic)


