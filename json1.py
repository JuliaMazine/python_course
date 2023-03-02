import json

itemList = []
dictionary = {}
with open('wikidata_1000.json', 'r', encoding='utf-8') as f:
    for jsonObj in f:
        itemList.append(json.loads(jsonObj))

    for item in itemList:
        key = item["label"]['value']
        try:
            value = item["description"]['value']
        except:
            value = 'None'
        dictionary[key] = value

        
with open('res1.json', 'w') as j:
    json.dump(dictionary, j, sort_keys=False, ensure_ascii=False, indent=4, separators=(',', ':'))

