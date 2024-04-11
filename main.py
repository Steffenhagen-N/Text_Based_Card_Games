suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.__suit_index = suits.index(suit)
        self.__rank_index = ranks.index(rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    # add
    # greater than
    # less than
    # equal
    # equal + suits
    # __stng__ description

class Deck_of_Cards:
    def __init__(self, low = True):
        self.__deck = []
        new_ranks = []
        
        for r in ranks:
            new_ranks.append(r)
        
        if low:
            pass
        if not low:
            new_ranks.remove("Ace")
            new_ranks.append("Ace")

        for suit in suits:
            for rank in new_ranks:
                self.__deck.append(Card(suit, rank))

    def shuffle(self):
        pass

    def draw(self):
        return self.__deck.pop()

class Card_Game:
    def __init__(self, low = True):
        self.deck = Deck_of_Cards(low)
    
    # create Deck_of_Cards
    # create player hand
    # create dealer hand

def main():
    my_deck = Deck_of_Cards()
    print(my_deck.draw())

main()