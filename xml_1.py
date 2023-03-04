import xml.etree.ElementTree as etree
tree = etree.parse("annot.opcorpora.no_ambig.xml")
root = tree.getroot()
with open("outputx.xml", 'w', encoding='utf-8') as f:
    for source in root.findall('.//source'):
        print(source.text, file=f)