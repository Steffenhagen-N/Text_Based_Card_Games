# while this isn't commented, the game will run twice
#from main import Card, Card_Game, Deck_of_Cards, go_fish
# comment before running, for debugging only

game = go_fish

game.initialize()
game.deck.shuffle()
game.player.draw(game.deck, 60)
print(game.player)

# try to make as many books as possible
# 'do you have any (kings, 7's, etc)'
# the other player must give you their copies
# if none, Go Fish! and draw a card
# if you draw the asked card, go again