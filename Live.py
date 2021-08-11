import GuessGame
import MemoryGame
import CurrencyRouletteGame

import Score

#Please choose a game to play:
#1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
#2. Guess Game - guess a number and see if you chose like the computer
#3. Currency Roulette - try and guess the value of a random amount of USD in ILS


def welcome(name):
    return "Hello {} and welcome to the world of games (WoG).\nHere you can find many cool games to play.".format(name)
    
def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    
    game = int(input("Choice: "))
    
    difficulty = int(input("Please choose game difficulty (1 to 5): "))

    if game == 1:
        win = GuessGame.play(difficulty)
    elif game == 2:
        win = MemoryGame.play(difficulty)
    elif game == 3:
        win = CurrencyRouletteGame.play(difficulty)
    else:
        print("Unknown game: {}".format(game))

    if win == True:
        Score.add_score(difficulty)
