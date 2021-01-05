import re

l = 'Beautiful is better than ugly.'
matchs = re.findall('beautiful',l,re.IGNORECASE)
print(matchs)

#%%文字検索

zen = '''Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea.Namespaces
are one honking
great idea -- let's
do more of those!'''

m = re.findall('^If',zen,re.MULTILINE)
print(m)

#%%複数候補の文字検索

string = 'Two too.'
m = re.findall('t[wo]o',string,re.IGNORECASE)
print(m)

#%%数字検索

line = '123 hi 45 hello.'
m = re.findall('\d',line,re.IGNORECASE)
print(m)

#%%非貪欲な正規表現

t = '_one__two__three_'
found = re.findall('_.*?_',t)
for match in found:
    print(match)

#%%特別な文字の一致

line_1 = 'I love $'
m = re.findall('\\$',line_1,re.IGNORECASE)
print(m)
