from random import shuffle

#カード単体での挙動
class Card:

    pictures = ['♤','♡','♢','♧']
    numbers = [None,None,2,3,4,5,6,7,8,9,10,'J','Q','K','A']

    def __init__(self,picture,number):
        self.p = picture
        self.n = number

    def __lt__(self,c2):
        if self.n < c2.n:
            return True
        elif self.n == c2.n:
            if self.p < c2.p:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self,c2):
        if self.n > c2.n:
            return True
        elif self.n == c2.n:
            if self.p > c2.p:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        a = '「' + self.pictures[self.p] + '」' + 'の' + '「' + str(self.numbers[self.n])+ '」'
        return a


#カード全体での挙動
class Deck:
    def __init__(self):
        self.cards = []

        for i in range(4):
            for j in range(2,15):
                self.cards.append(Card(i,j))

        shuffle(self.cards)

    def rm_card(self):
        if len(cards) == 0:
            return 'None'
        return self.cards.pop()

deck = Deck()


#プレイヤーの挙動
class Player:
    def __init__(self,name):
        self.name = name
        self.card = None
        self.win = 0


#ゲームの進行
player_1 = Player(input('プレイヤー名を入力してください。:'))
player_2 = Player('Computer')
i = 1
k = int(len(deck.cards) / 2)


for i in range(k):

    player_1.card = deck.cards[2 * i - 1]
    player_2.card = deck.cards[2 * i]
    #print(player_1.name + 'の選んだカードは' + str(player_1.card) + 'です。')
    #print(player_2.name + 'の選んだカードは' + str(player_2.card) + 'です。')

    if player_1.card > player_2.card:
        #print('おめでとう！' + player_1.name + 'の勝ちです。')
        player_1.win += 1

    else:
        #print('残念…。' + player_2.name + 'の勝ちです。')
        player_2.win += 1

print(player_1.name + 'の勝利数：' + str(player_1.win) + '回')
print(player_2.name + 'の勝利数：' + str(player_2.win) + '回')

if player_1.win > player_2.win:
    print('よってこの勝負、' + player_1.name + 'の勝ちです。\nおめでとうございます！')

elif player_1.win < player_2.win:
    print('よってこの勝負、' + player_2.name + 'の勝ちです。\nまた挑戦してください。')

else:
    print('よってこの勝負、引き分けです。\nまた挑戦してください。')
