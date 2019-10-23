import re

#
# s = "2019年10月1日举行国庆阅兵，庆祝建国70周年，祖国万岁。"
# pattern = r"\d+"
# r = re.search(r'\d+',s)
# print(r)

s = """Hello
北京
"""
# regex = re.compile(r'\w+')
# regex= re.compile(r'[a-z]+',flags=re.I)
# regex = re.compile(r'.+',flags=re.S)
regex = re.compile(r'Hello$', flags=re.M)
l = regex.findall(s)

print(l)

