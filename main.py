import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.__rank_value = 0
        self.__suit_index = suits.index(suit)
        self.__rank_index = ranks.index(rank)

        if type(self.rank) is int:
            self.__rank_value = self.rank
        if type(self.rank) is str:
            if self.rank == "Ace":
                self.__rank_value = 1
            if self.rank == "Jack" or "Queen" or "King":
                self.__rank_value = 10

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def __add__(self, card):
        return self.__rank_value + card.__rank_value
    
    def __sub__(self, card):
        return self.__rank_value - card.__rank_value

    def __gt__(self, card):
        if self.rank == card.rank:
            return self.__suit_index > card.__suit_index
        # figure out how to account for aces
        # right now aces are low, make them high

    def __lt__(self, card):
        pass
        # same issue as __gt__

    def __eq__(self, card):
        return self.suit ==card.suit and self.rank == card.rank


class Deck_of_Cards:
    def __init__(self, low = True):
        self.__deck = []
        new_ranks = []
        
        for r in ranks:
            new_ranks.append(r)
        
        if not low:
            new_ranks.remove("Ace")
            new_ranks.append("Ace")

        for suit in suits:
            for rank in new_ranks:
                self.__deck.append(Card(suit, rank))

    def __repr__(self):
        deck_list = []
        for card in self.__deck:
            deck_list.append(f"{card.rank} of {card.suit}")
        return ", " .join(deck_list)

    def shuffle(self):
        random.shuffle(self.__deck)

    def draw(self, hand, value = 1):
        for i in range(value):
            hand.append(self.__deck.pop())

class Player:
    pass
    #make hand
    #draw function
        
class Card_Game:
    def __init__(self, low = True):
        self.deck = Deck_of_Cards(low)
        player = Player
        dealer = Player

    def play(self):
        return ("There is nothing to play...")

def main():
    my_game = Card_Game()
    my_game.deck.shuffle()
    print(my_game.deck)

main()