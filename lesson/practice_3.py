#%%線形探索

def ss(k,n_list):
    found = False
    for i in n_list:
        if i == k:
            found = True
            break
    return found

numbers = range(1,100)

ss(1,numbers)
ss(100,numbers)

#%%回文判定

def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome('Mother'))
print(palindrome('Mom'))

#%%アナグラム

def anagram(word_1,word_2):
    w_1 = word_1.lower()
    w_2 = word_2.lower()
    return sorted(w_1) == sorted(w_2)

print(anagram('iceman','cinema'))
print(anagram('leaf','tree'))

#%%出現する文字をカウント

def word_count(text):
    count_dict = {}
    for word in text:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    print(count_dict)

word_count('soccer')
word_count('Dynasty')

#%%出現する文字をカウント その２

from collections import defaultdict

def count_characters(text):
    count_dict = defaultdict(int)
    for word in text:
        count_dict[word] += 1
    print(count_dict)

count_characters('soccer')

#%%出現する文字をカウント その３

from collections import Counter

print(Counter('soccer'))

#%%再帰

def bottles_of_beer(bob):

    if bob < 1:
        print('No more bottles of beer on the wall.\nNo more bottles of beer.')
        return

    tmp = bob
    bob -= 1
    print('''{} bottles of beer on the wall.
        {} bottles of beer.
        Take one down, pass it around,
        {} bottles of beer on the wall.'''.format(tmp,tmp,bob))
    bottles_of_beer(bob)

bottles_of_beer(10)

#%%再帰 練習問題

def fluits_eat(n):

    if n < 1:
        print('もうフルーツはありません。')
        return

    print('みかんが{}個あります。1個食べました。\nみかんは{}個になりました。'.format(n,n - 1))
    n -= 1
    fluits_eat(n)

fluits_eat(3)
