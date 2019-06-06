import re, datetime

s = "2019-05-29 10:41:54.977500"
d = datetime.datetime(*map(int, re.split('[^\d]', s)[:-1]))
print(d)
