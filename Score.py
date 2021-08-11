import os.path
import Util

def add_score(difficulty, filename='score.txt'):
    if not os.path.isfile(filename):
        with open(filename, 'a') as temp:
            temp.close()

    with open(filename, 'r+') as fp:
        score = fp.read()

        if not score:
            int_score = 0
        else:
            int_score = int(score)


        fp.seek(0)

        fp.write(str(int_score + ((difficulty*3) + 1)))


def get_score(filename):
    with open(filename, 'r') as fp:
        try:
            return int(fp.read())
        except ValueError:
            return None




if __name__ == '__main__':
    add_score(3, 'test.txt')
