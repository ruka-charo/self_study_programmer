#%%

class Orange:
    def __init__(self,w,c):
        '''重さは「グラム」'''
        self.weight = w
        self.color = c
        self.mold = 0
        print('Created!')

    def rot(self,day,temp):
        '''温度は摂氏'''
        self.mold = day * temp

orl = Orange(500,'dark orange')
print(orl)
print(orl.weight)
print(orl.color)


s = Orange(20,'yellow')
s.weight = 25
s.color = 'blue'
print(s.weight)
print(s.color)
print(s.mold)

s.rot(8,36)
print(s.mold)

#%%

class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self,w,l):
        self.width = w
        self.len = l

a = Rectangle(3,5)
print(a.width)
print(a.area())
a.change_size(4,6)
print(a.area())

#%%

class Data:
    def __init__(self):
        self.nums = [1,2,3,4,5]

    def change_data(self,index,n):
        self.nums[index] = n

data_1 = Data()
data_1.change_data(0,7)
print(data_1.nums)

#%%

class Shape:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def print_size(self):
        print('{} by {}'.format(self.width,self.len))

class Square(Shape):
    pass

my_shape = Shape(2,5)
my_shape.print_size()
a_square = Square(3,3)
a_square.print_size()

#%%

class Shape:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def print_size(self):
        print('{} by {}'.format(self.width,self.len))

class Square(Shape):
    def print_size(self):
        print('width = {},len = {}'.format(self.width,self.len))

    def area(self):
        return self.width * self.len

a_square = Square(3,3)
a_square.print_size()
print(a_square.area())

#%%

class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self,name):
        self.name = name

mick = Person('Mick Jagger')
stan = Dog('Stanley','Bulldog',mick)
print(stan.owner.name)

#%%

class Lion:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion('Jonney')
print(lion)

#%%

class Positive:
    def __init__(self,number):
        self.n = number

    def __add__(self,other):
        return abs(self.n + other.n)

x = Positive(-20)
y = Positive(5)

print(x + y)

#%%

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(another_bob is bob)
