

class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        # TODO: Initialize the bench object with whatever
        # attributes and values it will need
        self.players_on_bench = []

    def send_to_bench(self, player_name):
        # TODO: Put the player "onto the bench"
        self.players_on_bench.insert(0, player_name)

    def get_from_bench(self):
        # TODO: Return the name of the player who has
        # been on the bench longest.
        return self.players_on_bench.pop()

    # TODO: Write the function that will display the
    # current list of players on the bench
    def display_bench(self):
        print("The bench currently includes:")
        for player_name in self.players_on_bench:
            print(player_name)

    # TODO: Write any other methods that might be used
    # by the methods above.

    def remove_from_bench(self, player_name):
        if player_name in self.players_on_bench:
            self.players_on_bench.remove(player_name)
