import re

file = open('Indonesia.html', 'r', encoding='latin1')
pola = r'([\w+]+)</a></td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>([\d.\d\d]+)'

tuples = re.findall(pola, file.read())
tupp = [(t[0], float(t[1]))for t in tuples]
print (tupp)
