#%%独学プログラマー 問題

#P.116-5
def calculation(list_1,list_2):

    list_cal = []

    for number_1 in list_1:
        for number_2 in list_2:
            cal = number_1 * number_2
            print(str(number_1) + '×' + str(number_2) + '=' + str(cal) + 'です。')
            list_cal.append(cal)

    print(list_cal)


list_1 = [8,19,148,4]
list_2 = [9,1,33,83]

calculation(list_1,list_2)

#%%P.132

ans = input('好きな動物はなんですか？:')
sheet = open('/Users/rukaoide/Documents/Python/self_study_programmer/test.txt','w', encoding='utf-8')
sheet.write('好きな動物はなんですか？')
sheet.write('\n' + ans)
sheet.close()

#%%別解

ans = input('好きな動物はなんですか？:')
with open('/Users/rukaoide/Documents/Python/self_study_programmer/test.txt','w', encoding='utf-8') as f:
    f.write('好きな動物はなんですか？')
    f.write('\n' + ans)　

#%%

import csv

with open('/Users/rukaoide/Documents/Python/self_study_programmer/test.csv','w',encoding='utf-8',newline='') as f:
    w = csv.writer(f,delimiter=',')
    w.writerow(['Top Gun','Risky Business','Minority Report'])
    w.writerow(['Titanic','The Revenant','Inception'])
    w.writerow(['Training Day','Man on Fire','Flight'])
    w.writerow(['トップガン','リスキービジネス','マイノリティレポート'])
    w.writerow(['タイタニック','ザ・レベナント','インセプション'])
    w.writerow(['トレーニングデイ','マンオンファイアー','フライト'])

#%%P.156

import math

class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        return self.r * self.r * math.pi

circle_1 = Circle(2)
circle_2 = Circle(5)

print(circle_1.area())
print(circle_2.area())

#%%P.169

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2

class Square(Rectangle):
    def change_size(self,x):
        self.x = x
        return 'width:' + str(self.width + x) + '\nlength:' + str(self.length + x)

rectangle_1 = Rectangle(2,5)
square_1 = Square(3,3)

print(rectangle_1.calculate_perimeter())
print(square_1.calculate_perimeter())
print(square_1.change_size(2))

#%%コンポジション

class Rider:
    def __init__(self,name):
        self.name = name

class Horse:
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider

rider_1 = Rider('Mike')
horse_1 = Horse('John',rider_1)

print(horse_1.rider.name)

#%%P.215

import re

text = 'The ghost that says boo haunts the loo.'
found = re.findall('.oo',text)
for match in found:
    print(match)

#%%P.249

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        n = len(self.items) - 1
        return self.items[n]

    def size(self):
        return len(self.items)

stack_1 = Stack()
stack_2 = Stack()

def words_reverse(words):
    for word in words:
        stack_1.push(word)

    reverse = ''

    for i in range(stack_1.size()):
        reverse += stack_1.pop()

    print(reverse)

words_reverse('yesterday')

def list_reverse(list_):
    for word in list_:
        stack_2.push(word)

    reverse_l = []

    for i in range(stack_2.size()):
        reverse_l.append(stack_2.pop())


    print(reverse_l)

list_reverse([1,2,3,4,10])
