import random

deck = list('23456789JQKA'*4)
random.shuffle(deck)
value = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':10,'J':10,'Q':10,'K':10,'A':10}
player = [deck.pop() for _ in range(2)]

cpu = [deck.pop() for _ in range(2)]

#First two cards
print('Player Cards')
print(*player)
print('Dealer Cards')
print('* {}'.format(cpu[1]))


def check(who,hand):
    total = sum(map(value.get, player))
    if total > 21:
        print('{}You Loose.'.format(who))
    else:
        for card in player:
            if card == 'A':
                total += 10
                if total == 21:
                    print('{} wins.'.format(who))

    if len(hand) > 4:
        print('{} wins'.format(who),*hand)
        return False
    return True

while check('player', player) or check('CPU', player) :


    if(input('Enter to stay')):
        player.append(deck.pop())

