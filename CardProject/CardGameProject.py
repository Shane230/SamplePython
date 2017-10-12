import random

class Card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self,name,flag):
        self.name = name
        self.flag = flag
        if self.name=='dealer' and flag=='true':
            print('Hidden')
        else:
            print('{} of {}'.format(self.value, self.suit))

    def getCardValue(self):
        if(self.value =='A' or self.value =='J' or self.value =='K' or self.value =='Q'):
            self.value = 10
        else:
            self.value
        return self.value

class Deck(object):

    def __init__(self):
        self.firstTIme = 'True'
        self.deck = []
        self.player = []
        self.cpu = []
        self.build()
        self.shuffle()
        self.drawFirstTwoCard(self.firstTIme)
        self.showCards(self.player,self.cpu)

    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.deck.append(Card(s,v))

    def shuffle(self):
        for x in range(len(self.deck)-1,0,-1):
            r=random.randint(0,x)
            self.deck[x],self.deck[r] = self.deck[r],self.deck[x]

    def drawFirstTwoCard(self,firstTime):

        s1 = 0
        if firstTime == 'True':
            self.player = [self.deck.pop() for _ in range(2)]
        else:
            self.player.append(self.deck.pop())

        print('Player Cards')
        for c in self.player:
            c.show('player','false')
            s1=s1+ int(c.getCardValue())
        if firstTime == 'True':
            self.cpu = [self.deck.pop() for _ in range(2)]
        else:
            self.cpu.append(self.deck.pop())
        i=0
        s2=0
        print('Dealer Cards')
        for d in self.cpu:
            if(i==0):
                d.show('dealer','true')
                s2=s2+int(d.getCardValue())
            else:
                d.show('dealer', 'false')
                s2 = s2 + int(d.getCardValue())
            i+=1

        if s1==21 :
            print('***Player Won**')
            self.showCards(self.player,self.cpu)
            exit(0)
        elif s2==21 :
            print('****Dealer Won****')
            self.showCards(self.player, self.cpu)
            exit(0)
        else:
            print('Press H for Hit or S for stand')
            ans = input()
            self.drawFirstTwoCard('False')

    def showCards(self,player,cpu):
        print('+++Player Cards+++')
        for c in self.player:
            c.show('player','false')
        print('+++Dealer Cards+++')
        for d in self.cpu:
            d.show('Dealer', 'false')


card  = Deck()


