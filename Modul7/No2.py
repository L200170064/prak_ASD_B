import re

f = open('Indonesia.txt', 'r', encoding = 'latin1')
teks = f.read()
f.close

pola = r'di+\w+'

strings = re.findall(pola, teks)

print(strings)
