# while this isn't commented, the game will run twice
#from main import Card, Card_Game, Deck_of_Cards, blackjack
# comment before running, for debugging only

game = blackjack

game.initialize()
game.deck.shuffle()
game.player.draw(game.deck, 5)
print(game.player)

#try to get to 21 without going over