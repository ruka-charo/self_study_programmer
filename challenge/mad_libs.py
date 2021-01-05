import re

text = '''キリンは大昔から _複数名詞_ の興味の対象でした。
キリンは _複数名詞_ の中で一番背が高いですが、科学者たちは
そのような長い _体の一部_ をどうやって獲得したのか説明できません。キリンの
身長は _数値_ _単位_ 近くあり、その高さのほとんどは脚と _体の一部_ によるものです。'''

found = re.findall('_.*?_',text)
for match in found:
    word = input(match + 'に該当するものを入力してください:')
    print(match + ':' + word)
    text = text.replace(match,word)

print(text)
