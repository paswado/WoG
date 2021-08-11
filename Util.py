#!/usr/bin/env python3

import os
from sys import platform


SCORES_FILE_NAME='score.txt'
BAD_RETURN_CODE=-1


def screen_cleaner():
    if platform in ['linux', 'linux2', 'darwin']:
        os.system('clear')
    else:
        os.system('cls')

if __name__ == '__main__':
    screen_cleaner()
