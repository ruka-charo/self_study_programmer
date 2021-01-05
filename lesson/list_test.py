#%%要素の長さ

len([1,2,3,4,5,6])

#%%０から始まるリストの作成

List = range(10)
list(List)
print(list(List))
#リスト内要素の有る無し
5 in List
13 in List

#%%任意の長さのリストを作成

List = range(1,10)
list(List)
print(list(List))

#%%文字列の関数
A = 'Tokyo,America'
print(A.split(','))
print(A.split('o'))
print(A.index('e'))
#一文字目を「０」としている。
print(A.upper())

#%%要素の追加や削除
a = [1,2,3,4]

#追加
a.append(5)
print(a)

a.insert(1,1.5)
print(a)

#削除
a.pop(1)
print(a)

a.remove(3)
print(a)

#%%リストの足し算
t = [1,2,3]
s = [7,8,9]

print(t + s)

t.extend(s)
print(t)

#%%リスト要素の取り出し
u = [1,2,3,4,5,6,7,8,9]

u[0:3]
print(u[0:3])
u[1:5]
print(u[1:5])
u[3:]
print(u[3:])
u[:6]
print(u[:6])

#%%リスト要素の並び替え
v = [3,-1,5,9,-7]
w = ['mac','apple','alice','Piano']

#小さい順（アルファベット順）
v.sort()
print(v)
w.sort()
print(w)
#順番を逆転
v.reverse()
print(v)

#%%空のリストの作成
new_list = []
print(new_list)

#%%辞書型の呼び出し、追加、削除、空
country_code = {1:'America',39:'Itary',86:'China'}

#呼び出し
country_code[39]
print(country_code[39])
#追加
country_code[81] = 'Japan'
print(country_code)
#削除
country_code.pop(1)
print(country_code)
#空
new_dict = {}
print(new_dict)

#セット
list_set = set()
#追加
list_set.add(1)
list_set.add(2)
list_set.remove(1)
list_set

#リストのセット化
list_set_2 = set([1,2,2,5,7,10])
list_set_2
