import null

import Card

hand = Card()

def player(self,aName):
    self.name = aName
    self.emptyHand()

def emptyHand(self):
    for i in range(0,10):
        self.hand = null
    self.numCards = 0

def addCard(self,aCard=Card()):
    if self.numCards ==10:
        print(self.name+' hand already has 10 cards')
        exit(1)
    self.hand[self.numCards] =aCard
    self.numCards =+1

    return (self.getHandSum() <= 21);

def getHandSum(self):

    for c in range(0,self.numCards):
        cardNum = hand.


    for (int c=0;c < this.numCards; c++){
    cardNum = this.hand[c].getNumber();

    if (cardNum == 1 ){
    numAces++;
    handSum += 1;
    }else if (cardNum > 10){
    handSum += 10;
    }else{
    handSum += cardNum;
    }
    while (handSum > 21 & & numAces > 0){
    handSum -= 10;
    numAces--;
    }
    }

    return handSum;
