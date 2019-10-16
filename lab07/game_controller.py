from pair_of_dice import PairOfDice

INIT_NUM = 0
FIR_ROUND_LOSE_VALS = [2, 3, 12]
FIR_ROUND_WIN_VALS = [7, 11]
LOSE_VAL = 7


class GameController:
    '''A class representing a game controller'''
    def __init__(self):
        '''constructs a gamecontroller which record the point, current value
            and two dice'''
        self.my_point = INIT_NUM
        self.my_two_dice = PairOfDice()
        self.this_round = INIT_NUM

    def roll_dice(self):
        '''roll two dice every round
            GameController object -> None'''
        self.my_two_dice.roll_dice()
        self.this_round = self.my_two_dice.current_value()

    def check_fir_round_true(self):
        '''If user rolls FIR_ROUND_WIN_VALS on first roll, user wins
            GameController object -> Boolean'''
        if self.this_round in FIR_ROUND_WIN_VALS:
            return True
        return False

    def check_fir_round_false(self):
        ''' If user rolls FIR_ROUND_LOSE_VALS on first role, user loses
            GameController object -> Boolean'''
        if self.this_round in FIR_ROUND_LOSE_VALS:
            return False
        return True

    def check_ts_round_false(self):
        '''If user rolls LOSE_VAL, user loses
            GameController object -> Boolean'''
        if self.this_round == LOSE_VAL:
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
        if self.my_point == INIT_NUM:
            if self.check_fir_round_true():
                self.you_win(self.this_round)
            elif not self.check_fir_round_false():
                self.you_lose(self.this_round)
            else:
                self.my_point = self.this_round
                print("Your point is", self.my_point)
                self.lets_play()
        else:
            if self.check_ts_round_true():
                self.you_win(self.this_round)
            elif not self.check_ts_round_false():
                self.you_lose(self.this_round)
            else:
                print("You rolled " + str(self.this_round) + '.')
                self.lets_play()

    def you_lose(self, curr_val):
        print("You rolled " + str(curr_val) + ". You lose!")

    def you_win(self, curr_val):
        print("You rolled " + str(curr_val) + ". You win!")
