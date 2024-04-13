# Text Based Card Games

This is my first README, so bear with me as I try to make this both thorough and concise.

This project is an extensible framework for single-player text-based card games. The main.py file runs a rudimentary launcher menu, and holds the basic classes and functions needed for additional game files. Each supplimentary game file executes rules required for its corresponding game.

Text_Based_Card_Games was originally meant to be an exercise in Object Oriented Programming, and creating extensible programs. The program uses three classes; Cards, Decks, and Players; as efficiently as possible. As a challenge, I tried to repeat as little code as possible while still being clean to read. Ideally, as additional games are implemented, the main.py file shouldn't need to be changed much, if at all, to accomodate them. As Text_Based_Card_Games grows, hopefully bloat is kept to a minimum.


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


### Deck_of_Cards v.0.1

The Deck_of_Cards class constructor creates a single variable, an empty private deck list. This allows empty zones like hands and the discard pile to be classified as Decks. When called or printed, Decks return the number of cards, followed by a concatenated string of the card list (e.g. "-5 cards- 9 of Spades, 10 of Diamonds, 6 of Diamonds, 2 of Clubs, Ace of Hearts").

#### Implemented:

> ```py
> my_deck.generate(high = True):
> ```
> The generate function fills the Deck\__deck list with a full 52 card deck ranked low to high. The deck is unordered in case future programs need an ordered list, so most fresh generations will need to be shuffled. The optional argument determines whether aces are considered high or low, which is stored directly in the respective ace Card object. This way, the same game can have low and high aces. By default, aces are high.

### Player v.0.1
