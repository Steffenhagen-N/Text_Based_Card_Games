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

        # sets rank value to make math easier
        if type(self.rank) is int:
            self.__rank_value = self.rank
        if type(self.rank) is str:
            if self.rank == "Ace":
                self.__rank_value = 1
            if self.rank == "Jack" or "Queen" or "King":
                self.__rank_value = 10

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    # aces will always have a rank value of 1
    # specific programs have to compensate if aces are 
    # supposed to be worth 11
    def __add__(self, card):
        return self.__rank_value + card.__rank_value
    
    def __sub__(self, card):
        return self.__rank_value - card.__rank_value

    def __gt__(self, card):
        if self.rank == card.rank:
            return self.__suit_index > card.__suit_index
        return self.__rank_index > card.__rank_index

    def __lt__(self, card):
        if self.rank == card.rank:
            return self.__suit_index < card.__suit_index
        if self.rank == "Ace":
            return False
        if card.rank == "Ace":
            return True
        return self.__rank_index < card.__rank_index

    def __eq__(self, card):
        return self.suit ==card.suit and self.rank == card.rank

class Deck_of_Cards:
    def __init__(self):
        self.__deck = []

    # generates a full 52 card deck
    def generate(self, high = True):
        new_ranks = []
        for r in ranks:
            new_ranks.append(r)
        
        # changes low aces to high aces
        if high:
            new_ranks.remove("Ace")
            new_ranks.append("Ace")

        for suit in suits:
            for rank in new_ranks:
                self.__deck.append(Card(suit, rank))

    # prints deck as a single string rather than a list
    def __repr__(self):
        deck_list = []
        for card in self.__deck:
            deck_list.append(card.__repr__())
        return f"{len(self.__deck)} cards: {", " .join(deck_list)}"
    
    def get_deck(self):
        return self.__deck

    # add optioinal shuffle two decks together
    def shuffle(self, target = None):
        if target != None:
            target.top_to_deck(self, len(target.get_deck()))
        random.shuffle(self.__deck)

    def draw(self):
        return self.__deck.pop()
    
    def to_top(self, card):
        self.__deck.append(card)

    def top_to_deck(self, target, value = 1):
        for i in range(value):
            target.to_top(self.draw())
    
# add discard function
class Player:
    def __init__(self, name):
        self.__hand = Deck_of_Cards()
        self.__name = name

    def __repr__(self):
        return f"{self.__name}: {self.__hand.__repr__()}"

    def draw(self, deck, value = 1):
        for i in range(value):
            self.__hand.to_top(deck.draw())

    def get_name(self):
        return self.__name
    
    def get_hand(self):
        return self.__hand
        
class Card_Game:
    def __init__(self, filepath, high = True):
        self.__filepath = filepath
        self.deck = Deck_of_Cards()
        self.deck.generate(high)
        self.graveyard = Deck_of_Cards()
        self.player = Player("Player 1")
        self.dealer = Player("The Dealer")

    def run(self):
        exec(open(self.__filepath).read())

# list of all the games currently supported
# allows for clean game.run() in main()
blackjack = Card_Game("blackjack.py")
go_fish = Card_Game("go_fish.py")
solitaire = Card_Game(None)
war = Card_Game(None)
games = [blackjack, go_fish]

def main():
    print("game status...")
    print("")
    # this is how specific games will be run by the main file
    #blackjack.run()
    #go_fish.run()
    for g in games:
        g.run()
        
    print("")

    print("--- testing new game ---")
    print("")
    print("generating deck...")
    print("")
    my_game = Card_Game(None)
    print("--- deck ---")
    print(my_game.deck)
    print("")
    print("shuffling...")
    print("")
    my_game.deck.shuffle()
    print("--- deck ---")
    print(my_game.deck)
    print("")
    print("milling several cards...")
    my_game.deck.top_to_deck(my_game.graveyard, 10)
    print("")
    print("--- deck ---")
    print(my_game.deck)
    print("")
    print("--- graveyard ---")
    print(my_game.graveyard)
    print("")
    print("reshuffling deck and graveyard...")
    print("")
    my_game.deck.shuffle(my_game.graveyard)
    print("--- deck ---")
    print(my_game.deck)
    print("")
    print("--- graveyard ---")
    print(my_game.graveyard)

main()