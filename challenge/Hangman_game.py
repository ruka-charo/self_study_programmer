#ゲーム「ハングマン」

#文字列の準備
player_word = 'Ruka'.lower()
words = list(player_word)
words_ans = list(player_word)
board = ['_']*len(words)

#プレイヤー
stage = ['______      ',     #プレイヤー1の描写
         '|     |     ',
         '|     |     ',
         '|   \ O /   ',
         '|     |     ',
         '|    / \    ',
         '|___________'
         ]
wrong = 0                   #プレイヤー2のミス回数


print('ハングマンへようこそ！')

while wrong < 7 and board != words_ans:
    i = 0
    player_2 = input('文字を1文字入力してください。:')

    #該当なし
    if player_2 not in words:
        wrong += 1
        print(board)
        for i in range(wrong):
            print(stage[i])

    #該当あり
    elif player_2 in words:
        for word in words:

            if player_2 == word:
                board[i] = words[i]
                words[i] = '/'
                print(board)

            elif player_2 != word:
                i += 1

if wrong == 7:
    print('残念…。あなたの負けです。\n正解は「' + player_word +'」でした。')
elif board == words_ans:
    print('おめでとうございます！あなたの勝ちです。')
