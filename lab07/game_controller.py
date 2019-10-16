from pair_of_dice import PairOfDice


class GameController:
    '''A class representing a game controller'''
    def __init__(self):
        '''constructs a gamecontroller which record the point, current value
            and two dice'''
        self.my_point = 0
        self.my_two_dice = PairOfDice()
        self.this_round = 0

    def roll_dice(self):
        '''roll two dice every round
            GameController object -> None'''
        self.my_two_dice.roll_dice()
        self.this_round = self.my_two_dice.current_value()

    def check_fir_round_true(self):
        '''If user rolls 7 or 11 on first roll, user wins
            GameController object -> Boolean'''
        if self.this_round == 7 or self.this_round == 11:
            return True
        return False

    def check_fir_round_false(self):
        ''' If user rolls 2, 3, or 12 on first role, user loses
            GameController object -> Boolean'''
        if (self.this_round == 2 or self.this_round == 3 or
                self.this_round == 12):
            return False
        return True

    def check_ts_round_false(self):
        '''If user rolls 7, user loses
            GameController object -> Boolean'''
        if self.this_round == 7:
            return False
        return True

    def check_ts_round_true(self):
        '''If user rolls point again, user wins
            GameController object -> Boolean'''
        if self.this_round == self.my_point:
            return True
        return False

    def lets_play(self):
        '''start playing
            GameController object -> None'''
        print("Press enter to roll the dice...")
        self.roll_dice()
        input()
        if self.my_point == 0:
            if self.check_fir_round_true():
                print("You rolled " + str(self.this_round) + ". You win!")
            elif not self.check_fir_round_false():
                print("You rolled " + str(self.this_round) + ". You lose!")
            else:
                self.my_point = self.this_round
                print("Your point is", self.my_point)
                self.lets_play()
        else:
            if self.check_ts_round_true():
                print("You rolled " + str(self.this_round) + ". You win!")
            elif not self.check_ts_round_false():
                print("You rolled " + str(self.this_round) + ". You lose!")
            else:
                print("You rolled " + str(self.this_round) + '.')
                self.lets_play()
