import null as null

import Suit
import Card
import random


class Deck:
    myCards = []

    # aSuit = Suit()

    def __init__(self):
        print('default constructor')
        self.assignNumDecksShuffleValue(1, 'false')

    def assignNumDecksShuffleValue(self, numdecks, shuffle):
        self.numCards = numdecks * 52
        self.shuffle = shuffle
        myCards = [self.numCards]

        c = 0

        for d in range(1, numdecks):
            for s in range(1, 4):
                for n in range(1, 13):
                    obj = Deck(Suit.value[s], n)
                    self.myCards[c] = obj;
                    c += 1

        if shuffle:
            self.shuffle()

    def shuffle(self):
        temp = Card()

        for i in range(0, self.numCards):
            j = random.randint(self.numCards)
            temp = self.myCards[i]
            self.myCards[i] = self.myCards[j]
            self.myCards[j] = temp

    def dealNextCard(self):
        top = Card(self.myCards[0])

        for c in range(1, self.this.numCards):
            self.myCards[c - 1] = self.myCards[c]

        self.myCards[self.numCards - 1] = null;
        self.numCards =-1;

        return top
