import json
import collections
cnt = collections.Counter()
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for j in range(len(data['acts'])):
        for k in range(len(data['acts'][j]['scenes'])):
            for l in range(len(data['acts'][j]['scenes'][k]['action'])):
                       cnt[data['acts'][j]['scenes'][k]['action'][l]['character']] += len(data['acts'][j]['scenes'][k]['action'][l]['says'])
print(cnt)




