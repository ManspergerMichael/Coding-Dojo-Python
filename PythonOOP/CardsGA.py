#My code
import random
class Deck(object):
    def __init__(self):
        self.deck = []
        suits = ['spades','hearts','clubs','diamond']
        for suit in suits:
            for x in range(1,14):
                self.deck.append(card(x,suit))
    def deal(self):
        for i in range(len(self.deck)):
            print self.deck[i].suit, self.deck[i].value
    def shuffle(self):
        for x in range(0, len(self.deck)):
            rand_indx = random.randint(0,51)
            temp = self.deck[x]
            self.deck[rand_indx]=temp


class card(object):
    def __init__(self,num,suit):
        self.suit = suit
        self.value = num
    def __str__(self):
        return "This is the {} of {}".format(self.value,self.suit)

'''
suits = ['spades','hearts','clubs','diamond']
for suit in suits:
    for x in range(1,14):
        deck.append(card(x,suit))
'''

newDeck = Deck()
newDeck.shuffle()
newDeck.deal()

#demo Code
'''
class Card(object):
    def __init__(self,suit,val):
        self.suit = suit
        self.val = val

class Deck(object):
    def __init__(self):
        self.deck_list = []
        suits = ['spades','hearts','clubs','diamond']
        for suit in suits:
            for x in range(2,15):
                self.deck_list.append(card(x,suit))
'''