# Using: https://pypi.org/project/CurrencyConverter/

from currency_converter import CurrencyConverter
from random import randrange

import score

def get_money_interval(usd_value, difficulty):
    c = CurrencyConverter()

    # Round to 2 digits after the '.', allows edge case guesses to be correct more easily
    ils_value = int((c.convert(usd_value, 'USD', 'ILS'))*100)/100

    return (ils_value - (5 - difficulty), ils_value + (5 - difficulty))


def get_guess_from_user(usd_value):
    return float(input("Guess how much {} USD is worth in ILS: ".format(usd_value)))


def play(difficulty):
    usd_value = randrange(1, 100)

    ils_value_range = get_money_interval(usd_value, difficulty)
    ils_value_guess = get_guess_from_user(usd_value)

    if ils_value_guess >= ils_value_range[0] and ils_value_guess <= ils_value_range[1]:
        print("Your guess is correct! You win!")
        return True
    else:
        print("Meh, loser")
        return False




if __name__ == '__main__':
    play(3)
