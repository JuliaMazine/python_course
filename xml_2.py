import xml.etree.ElementTree as etree
tree = etree.parse("annot.opcorpora.no_ambig.xml")
root = tree.getroot()
list = []
with open("xml2.txt", "w", encoding='utf-8') as f:
    for token in root.findall('.//token'):
        for g in token.iter('g'):
            list.append(g.attrib['v'])
        if 'NOUN' in list and 'plur' in list:
            f.write(token.attrib['text'] + ' ')





