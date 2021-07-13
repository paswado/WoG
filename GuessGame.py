import random
import math


def generate_number(difficulty):
    return random.choice(range(1, difficulty + 1))


def compare_result(user_input, r):
    return user_input - r


def play(difficulty):
    # Assuming getting input is part of the game? Otherwise can pass as arg
    try:
        user_input = int(input("Guess a number between 1 and {}: ".format(difficulty)))
    except ValueError as e:
        print("You done goofed: {}".format(str(e.args)))
        return False

    r = generate_number(difficulty)
    print(r)

    res = compare_result(user_input, r)

    if res == 0:
        print("You win!")
        return True
    else:
        print("You lose! You were off by {}".format(abs(res)))
        return False


if __name__ == "__main__":
    play(5)

