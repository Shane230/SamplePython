import Suit
class Card:

    aSuit  = Suit()

    def __int__(self,aSuit,aNumber):
        self.aSuit = aSuit
        self.aNumber = aNumber

        if aNumber >=1 and aNumber <= 13:
            self.myNumber = aNumber
        else:
            print(aNumber +'is invalid number')
            exit(1)

    def getNumber(self):
        return self.myNumber

    def __str__(self,myNumber):

        if self.myNumber == 1:
            numStr = 'Ace'
        elif self.myNumber == 2:
            numStr = 'Two'
        elif self.myNumber == 3:
            numStr = 'Three'
        elif self.myNumber == 4:
            numStr = 'Four'
        elif self.myNumber == 5:
            numStr = 'Five'
        elif self.myNumber == 6:
            numStr = 'Six'
        elif self.myNumber == 7:
            numStr = 'Seven'
        elif self.myNumber == 8:
            numStr = 'Eight'
        elif self.myNumber == 9:
            numStr = 'Nine'
        elif self.myNumber == 10:
            numStr = 'Ten'
        elif self.myNumber == 11:
            numStr = 'Jack'
        elif self.myNumber == 12:
            numStr = 'Queen'
        elif self.myNumber == 13:
            numStr = 'King'

        return numStr + 'of' + str(self.aSuit)
