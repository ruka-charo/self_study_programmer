#%% 繰り返し出力
for i in range(20):
    print('ご無沙汰しております。')

10 != 100

#%%

def f(x,y):
    return x + y
f(2,6)

#%%　グローバル変数

x = 3
def f():
    global x
    x = x + 1
    print(x)
f()

#%%　例外処理

try:
    a = int(input('分母を入れてください。:'))
    b = int(input('分子を入れてください。:'))

    print(b / a)
except (ZeroDivisionError,ValueError):
    print('適切な入力をしてください。')

#%%　メゾット一例

import datetime
today = datetime.date.today()
birthday = datetime.date(1996,1,20)
print(today - birthday)

#%%リスト

fluits = ['apple','orange','grape']
fluits.append('Peach')
fluits[1]

index = 1
for fluit in fluits:
    print(str(index) + '：' + fluit)
    index = index + 1

#%%　リスト追加、削除

fluits = ['apple','orange','grape']
fluits.append('Peach')
sports = ['tennis','soccer','baseball','running']
sports.pop()
print(fluits + sports)

print('Peachはリスト内にありますか？')
print('Peach' in fluits)
print('runningはリスト内にありますか？')
print('running' in sports)

len(fluits)

lists = []
lists.append(fluits)
lists.append(sports)
lists[0]

#%%　タプル、辞書

fluits = ('apple','orange','grape')
fluits[0]
fluits[-1]

sports = {'soccer':'嫌い','tennis':'好き','野球':'普通'}
sports['tennis']
sports['basketball'] = '普通'
sports
'tennis' in sports
del sports['soccer']
sports

lists = []
lists.append(fluits)
lists.append(sports)
lists

#%%　リスト内にリスト

games = {
    'PS4':['Devil May Cry5','Monster Hunter World','Sword Art Online'],
    'Review':{'Devil May Cry5':'面白い','Monster Hunter World':'とても面白い','Sword Art Online':'とてもワクワクする'}
}

games

ny = {
    '座標':(40.7128,74.0059),
    'セレブ':['ウッディ・アレン','ジェイ・Z','ケビン・ベーコン'],
    '事実':{'州':'ニューヨーク','国':'アメリカ'}
}

#%%　文字列

'My' + ' name' + ' is' + ' Ruka!'
'hello ' * 3
'my name is Ruka!'.upper()
'MY NAME IS RUKA'.lower()
'my name is Ruka!'.capitalize()
'abababab'.replace('b','a')
"こんにちは、{}".format("みなさん")

who = input('誰に？:')
when = input('いつ？:')

"こんにちは、{}。{}は頑張ろう！".format(who,when)

'こんにちは。今日もいい天気ですね！'.split('。')

'+'.join('abc')
'+'.join(['a','b','c'])
' The   '.strip()
'abcdefghijk'.index('f')

print('一行目\n二行目\n三行目')

word = 'abcdefghijk'
word[2:6]
word[:4]
word[2:]

dict = ['a','b','c','d']
dict[1:3]

#%% for文

lists = ['tennis','baseball','swimming']

i = 0
for sport in lists:
    new = lists[i].upper()
    lists[i] = new
    i += 1

print(lists)

#%% fot文(有名手法)

lists = ['tennis','baseball','swimming']

for i, sport in enumerate(lists):
    new = lists[i].upper()
    lists[i] = new

print(lists)

#%%　for文

for i in range(1,11):
    print(i)
    print('繰り返し出力の原理')

#%% while文

x = 10
while x > 0:
    print(x)
    x -= 1
print('Happy New Year!')

#%% モジュール

import random
random.randint(1,50)

import statistics
nums = [1,4,21,5,-3,9,-12,5]

statistics.mean(nums)
statistics.median(nums)
statistics.mode(nums)

import keyword

keyword.iskeyword('for')
keyword.iskeyword('run')

import module1
module1.hello()

#%%
