from die import Die


class PairOfDice:
    '''A class representing pairs of dice'''
    def __init__(self):
        '''create two dice
            PairOfDice object -> None'''
        self.die_1 = Die()
        self.die_2 = Die()

    def roll_dice(self):
        '''roll two dice
            PairOfDice object -> None'''
        self.die_1.roll()
        self.die_2.roll()

    def current_value(self):
        '''return current value
            PairOfDice object -> number'''
        return self.die_1.current_value + self.die_2.current_value
