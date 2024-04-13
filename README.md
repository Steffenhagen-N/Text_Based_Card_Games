# Text Based Card Games

This is my first README, so bear with me as I try to make this both thorough and concise.

This project is an extensible framework for single-player text-based card games. The main.py file runs a rudimentary launcher menu, and holds the basic classes and functions needed for additional game files. Each supplimentary game file executes rules required for its corresponding game.

Text_Based_Card_Games was originally meant to be an exercise in Object Oriented Programming, and creating extensible programs. The program uses four classes; Cards, Decks, Players, and Games; as efficiently as possible. As a challenge, I tried to repeat as little code as possible while still being clean to read. Ideally, as additional games are implemented, the main.py file shouldn't need to be changed much, if at all, to accomodate them. As Text_Based_Card_Games grows, hopefully bloat is kept to a minimum.


## Build Status v.0.0.1

Text_Based_Card_Games is currently in a prototype stage. No games are currently implemented, and the menu and launcher are still under construction. Classes are mostly finished, and can interact with eachother. Test scenarios can be hard-coded into the main function. Planned games include:
-Go Fish
-Blackjack
-War


## Main Class Functionality

This is a list of all callable main class functions both currently implemented and planned. This section acts as a Help guide for implementation of additional games using the existing framework.


### Card v.1.0

The Card class constructor creates public suit and rank variables, and private rank value, rank index, and suit index variables. When called or printed, Cards return the string "{rank} of {suit}" (e.g. "Ace of Spades"). Cards have no callable methods, but arithmatic operators have been overloaded.

#### Implemented:

> ```py
> my_card1 + my_card2 >>> int()
> my_card1 - my_card2 >>> int()
> ```
> Addition and subtraction compare the two Card.\__rank_value variables and return one integer. Rank value for face cards are naturally set to 10, and ace cards are set to 1. This is used in blackjack.py to determine the numerical value of dealt cards.

> ```py
> my_card1 > my_card2 >>> bool()
> my_card1 < my_card2 >>> bool()
> my_card1 = my_card2 >>> bool()
> ```
> Greater than and less than return a boolean value comparing the Card.\__rank_index variables of both cards. If the rank indexes are equal, it will compare the Card.\__suit_index variables instead.
> For example, ("6 of Hearts" > "6 of Clubs") will return True.

#### Planned:

As of Card v.1.0, no future functions or variables are planned.


### Deck_of_Cards v.1.0

The Deck_of_Cards class constructor creates a single variable; an empty private deck list. This allows empty zones like hands and the discard pile to be classified as Decks. When called or printed, Decks return the number of cards, followed by a concatenated string of the card list (e.g. "-5 cards- 9 of Spades, 10 of Diamonds, 6 of Diamonds, 2 of Clubs, Ace of Hearts").

#### Implemented:

> ```py
> my_deck.generate(high = True):
> ```
> Fills list my_deck.\__deck with all 52 cards ranked low to high. The deck is unordered in case future programs need an ordered list, so most fresh generations will need to be shuffled. The optional argument determines whether aces are considered high or low, which is stored directly in the respective ace Card object. This way, the same game instance can have low and high aces. By default, aces are high.

>```py
> my_deck.get_deck():
> ```
> Returns list my_deck.\__deck.

> ```py
> my_deck.shuffle(optional_deck = None):
> ```
> Shuffles list my_deck.\__deck. The optional argument allows for another optional_deck (without .\__deck suffix) to be shuffled into my_deck.\__deck. This can be used to shuffle the discard pile or hand into the main deck.

> ```py
> my_deck.draw():
> ```
> Pops the top card of my_deck. This isn't how players should draw cards, this function is mainly used to facilitate other functions. 

> ```py
> my_deck.to_top(my_card):
> ```
> Puts Card my_card on top of my_deck.\__deck. Like .draw(), this function is mainly used for other functions, but has some applicability in returning cards from a player hand to the main deck.

> ```py
> my_deck.top_to_deck(target_deck, value = 1):
> ```
> Transfers cards from the top of my_deck to the top of Deck target_deck. The function defaults to a single card, but has the ability to transfer multiple cards (e.g. putting the top 10 cards of the main deck into the graveyard). If my_deck runs out of cards in the middle of the loop, the loop breaks and prints "Out of cards!".

#### Planned:

As of Deck_of_Cards v.1.0, no future functions or variables are planned.


### Player v.0.1

The Player class constructor creates two private variables; a hand classified as Deck_of_Cards, and a name. When called or printed, Players return a string of their name, followed by a concatenated string of their hand.

#### Implemented:

> ```py
> player1.draw(my_deck, value = 1):
> ```
> The top x cards of my_deck (without .\__deck suffix) are put into the hand of player1. 


### Card_Game v.0.1
