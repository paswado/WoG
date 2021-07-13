#!/usr/bin/env python3

from sys import platform as _platform
from os import system as call

from Live import load_game, welcome


if __name__ == "__main__":
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        call("clear")
    else:
        call("cls")
        

    name = "something or other"
    
    print(welcome(name), end='\n\n')
    load_game()


