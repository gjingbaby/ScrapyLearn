import random

deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11] * 4   #列表内元素重复四次
'''
shuttle函数将列表内随机排序
没有返回值
'''
random.shuffle(deck)

d_cards = []
p_cards = []
#print('deck has '+str(len(deck))+' cards')
while len(d_cards) != 2:
    random.shuffle(deck)
    d_cards.append(deck.pop())
    if len(d_cards) == 2:
        print('the card dealer has are ',d_cards)
while len(p_cards) != 2:
    random.shuffle(deck)
    p_cards.append(deck.pop())
    if len(p_cards) == 2:
        print('the total player is',sum(p_cards))
        print('the cards player has are',p_cards)

#print('deck has '+str(len(deck))+' cards')

if sum(p_cards) > 21:
    print("you are BUSTED!\n  *************dealer wins*************")
    exit()

if sum(d_cards) > 21:
    print("dealer is busted!\n  *************you are the winner*************")
    exit()

if sum(d_cards) == 21:
    print("dealer wins \n  *************dealer wins*************")
    exit()

if sum(d_cards) == 21 and sum(p_cards) == 21:
    print("match")
    exit()


def dealer_choice():
    if sum(d_cards) < 17:
        while sum(d_cards) < 17:
            random.shuffle(deck)
            d_cards.append(deck.pop())
    print("Dealer has total " + str(sum(d_cards)) + "with the cards ", d_cards)

    if sum(p_cards) == sum(d_cards):
        print("match")
        exit()

    if sum(d_cards) == 21:
        if sum(p_cards) < 21:
            print("dealer wins")
        elif sum(p_cards) == 21:
            print("match")
        else:
            print("dealer wins")
    elif sum(d_cards) < 21:
        if sum(p_cards) < 21 and sum(p_cards) < sum(d_cards):
            print("dealer wins")
        elif sum(p_cards) < 21 and sum(p_cards) > sum(d_cards):
            print("player wins")
        else:
            print('dealer wins')

    else:
        if sum(p_cards) < 21:
            print("player wins")
        elif sum(p_cards) == 21:
            print('palyer wins')
        else:
            print('dealer wins')


while sum(p_cards) < 21:
    k = input('Want to hit or stay?\n Press 1 for hit and 0 for stay')
    if k == 1:
        random.shuffle(deck)
        p_cards.append(deck.pop())
        print('You have a total of ' + str(sum(p_cards))
              + ' with the cards ', p_cards)
        if sum(p_cards) == 21:
            print("player wins")
        if sum(p_cards) > 21:
            print('player lose')
    else:
        dealer_choice()
        break


