import os.path

def add_score(filename='score.txt'):
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

        fp.write(str(int_score + 1))


if __name__ == '__main__':
    add_score('test.txt')
