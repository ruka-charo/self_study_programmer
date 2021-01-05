#%%

import os
os.path.join('Users','Documents','python')

st = open('/Users/rukaoide/Documents/Python/st.txt','w')
st.write('Hello!')
st.close()

st = open('/Users/rukaoide/Documents/Python/st.txt','w',encoding='utf-8')
st.write('こんにちは！')
st.close()

with open('/Users/rukaoide/Documents/Python/st.txt','w') as st:
    st.write('Hello! My name is Ruka.')

lists = []
with open('/Users/rukaoide/Documents/Python/st.txt','r') as st:
    lists.append(st.read())
    print(st.read())

print(lists)

#%%

import csv

#オブジェクト　→　csv
with open('/Users/rukaoide/Documents/Python/ex.csv','w',newline = '') as f:
    w = csv.writer(f,delimiter = ',')
    w.writerow([1,2,3])
    w.writerow(['one','two','three'])

#csv　→　オブジェクト
with open('/Users/rukaoide/Documents/Python/ex.csv','r') as f:
    r = csv.reader(f,delimiter = ',')
    for row in r:
        print(','.join(row))

#%%
