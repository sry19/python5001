import random

RANDOM_START = 1
RANDOM_END = 6
INIT = 0


class Die:
    '''A class representing a Die'''
    def __init__(self):
        '''create a die object, initialize its value as 0'''
        self.current_value = INIT

    def roll(self):
        '''roll a die
            Die object -> None'''
        self.current_value = random.randint(RANDOM_START, RANDOM_END)
