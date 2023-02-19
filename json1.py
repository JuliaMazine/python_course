import json

itemList = []
with open('wikidata_1000.json', 'r', encoding='utf-8') as f:
    for jsonObj in f:
        itemDict = json.loads(jsonObj)
        itemList.append(itemDict)

with open('res1.json', 'w') as j:
    for item in itemList:
        try:
            json.dump({item["label"]['value']: item["description"]['value']}, j, ensure_ascii=False, indent=4)
        except:
            json.dump({item["label"]['value']: 'None'}, j, ensure_ascii=False, indent=4)
