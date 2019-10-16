

class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        '''construct a bench which has players' list on the bench'''
        self.players_on_bench = []

    def send_to_bench(self, player_name):
        '''add a player to the bench'''
        self.players_on_bench.insert(0, player_name)

    def get_from_bench(self):
        '''remove a player who rested longest from the bench'''
        return self.players_on_bench.pop()

    def display_bench(self):
        '''display all players on the bench'''
        print("The bench currently includes:")
        for player_name in self.players_on_bench:
            print(player_name)

    def remove_from_bench(self, player_name):
        '''remove a specific player from the bench'''
        if player_name in self.players_on_bench:
            self.players_on_bench.remove(player_name)
