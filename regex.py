import re

s = "Alex:1994,Sunny:1996,Tony:1995,Dick:1993"
pattren = re.compile(r"(\w+):(\d+)")

regex = re.compile(pattren)
a = regex.findall(s, 0, 15)
print(dict(a))

l = re.split(r"[:,]",s,2)
print(l)
p = re.subn(r':',' ',s)
print(p)
