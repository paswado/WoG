import time
import random
import shutil

def _print(str, delay=0.7):
    str_len = len(str)

    blank_str = "{}{}".format('\b' * str_len,' ' * str_len)


    print(str, end='', flush=True)
    time.sleep(delay)
    print(blank_str, flush=True)


def generate_sequence(difficulty):
    numbers = []

    for i in range(1,difficulty + 1):
        numbers.append(random.randrange(1,101))

    return numbers


def get_list_from_user():
    return input("Remember the numbers? (Input a space delimited list of numbers)\n").split(' ')


def list_is_equal(random_numbers, user_numbers):
    # Not sure if more efficient than compaing two lists
    # but definitely easier

    try:
        for i in range(len(random_numbers)):
                if int(random_numbers[i]) != int(user_numbers[i]):
                    return False
    except IndexError as e:
        print("Looks like you didn't remember all the numbers, guess you lose... loser.")

        exit(1)

    return True

def play(difficulty):
    if difficulty >= 1 and difficulty <= 5:
        print("Playing on difficulty {}".format(difficulty))
    else:
        print("Bad difficulty: {}".format(difficulty))
        return 1

    random_numbers = generate_sequence(difficulty)

    _print(' '.join([str(i) for i in random_numbers]))

    user_numbers = get_list_from_user()

    if list_is_equal(random_numbers, user_numbers):
        print("You win!")
        return True
    else:
        print("You lose!")
        return False


if __name__ == '__main__':
    d = int(input("Choose difficulty: "))

    play(d)
