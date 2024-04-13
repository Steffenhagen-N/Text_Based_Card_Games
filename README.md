# Text Based Card Games

This project is an extensible framework for single-player text-based card games. The main.py file runs a rudimentary launcher menu, and holds the basic classes and functions needed for additional game files. Each supplimentary game file executes rules required for its corresponding game.

Text_Based_Card_Games was originally meant to be an exercise in Object Oriented Programming, and creating extensible programs. The program uses three classes; Cards, Decks, and Players; as efficiently as possible. As a challenge, I tried to repeat as little code as possible while still being clean to read. Ideally, as additional games are implemented, the main.py file shouldn't need to be changed much, if at all, to accomodate them. Theoretically, Text_Based_Card_Games is infinitely expandable without getting too bloated.


## Build Status v.0.0.1

Text_Based_Card_Games is currently in a prototype stage. No games are currently implemented, and the menu and launcher are still under construction. Classes are mostly finished, and can interact with eachother. Test scenarios can be hard-coded into the main function. Planned games include:
-Go Fish
-Blackjack
-War


## Main Class Functionality

This is a list of all callable main class functions both currently implemented and planned. This section acts as a Help guide for implementation of additional games using the existing framework.


### Card v.1.0

The Card class constructor creates public suit and rank variables, and private rank value, rank index, and suit index variables. When the class is returned or printed, it will return as "{rank} of {suit}". Cards have no callable methods, but arithmatic operators have been overloaded.

#### Implemented:

> ```py
> Card1 + Card2 >>> int()
> Card1 - Card2 >>> int()
> ```
> Addition and subtraction compare the two private card.\__rank_value variables and return one integer. Rank value for face cards are naturally set to 10, and ace cards are set to 1. This is used in blackjack.py to determine the numerical value of dealt cards.

```py
Card1 > Card2 >>> bool()
Card1 < Card2 >>> bool()
Card1 = Card2 >>> bool()
```


### Deck_of_Cards v.0.1

### Player v.0.1
