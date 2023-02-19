import json
counter_dict = {}
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for j in range(len(data['acts'])):
        for k in range(len(data['acts'][j]['scenes'])):
            for l in range(len(data['acts'][j]['scenes'][k]['action'])):
                    if data['acts'][j]['scenes'][k]['action'][l]['character'] not in counter_dict:
                        counter_dict[data['acts'][j]['scenes'][k]['action'][l]['character']] = 0
                    else:
                        counter_dict[data['acts'][j]['scenes'][k]['action'][l]['character']] += 1
print(max(counter_dict, key=counter_dict.get))
