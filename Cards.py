class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["zero", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank]) + " of " + (self.suits[self.suit])

    def cmp(self,other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range (1,14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + str(self.cards[i])  + "\n"
        return s

    def shuffle(self):
        import random
        rng = random.Random()
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = rng.randrange(i, num_cards)
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])
        t = ""
        for i in range((num_cards)):
            t = t + str(self.cards[i]) + "\n"
        return(t)

    def pop(self):
        return self.cards.pop()

rd = Deck()
Shuffleddeck = rd.shuffle()
print(Shuffleddeck)

# String Version
# u = []
# for i in range((num_cards)):
#     u = self.cards[i]
# return [u]