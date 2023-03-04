import json
characters = list()
with open('RomeoAndJuliet.json', 'r') as f:
    data = json.load(f)
    for j in range(len(data['acts'])):
        for k in range(len(data['acts'][j]['scenes'])):
            chars_in_scene = set()
            for l in range(len(data['acts'][j]['scenes'][k]['action'])):
                chars_in_scene.add(data['acts'][j]['scenes'][k]['action'][l]['character'])
            chars_in_scene = list(chars_in_scene)
            characters.append(chars_in_scene)
print(characters)
with open('res2.json', 'w') as q:
    for i in characters:
        q.write(json.dumps(i))
        q.write("\n")


