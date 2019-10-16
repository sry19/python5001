from player import Player


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.
    def set_team_name(self, name):
        # TODO: set the team name
        self.name = name

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        # TODO: call the Player class constructor with the appropriate
        # values to create a new player object, then add that
        # player object to the team's players list.
        new_player = Player(player_name, player_number, player_position)
        self.players.append(new_player)

    def cut_player(self, player_name):
        # TODO: Remove the player with the name player_name
        # from the players list.
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                return

    def is_position_filled(self, position):
        # TODO: Write the method that checks whether
        # there is currently at least one player on the team
        # occupying the requested position
        for player in self.players:
            if player.position == position:
                return True
        return False

    # TODO: Write any necessary methods to support the methods
    # above, and write the method that will display (print to screen)
    # the full team roster in the following format:
    def show_team_member(self):
        print("The lineup for", self.name, "is:")
        if not self.players:
            print("The team currently has no players")
            return
        for player in self.players:
            print("{0:<4}  {1:<15}  {2:<11}".format(player.number,
                                                    player.name,
                                                    player.position))
    #    The lineup for Seattle Scorpions is:
    #    15       Garcia          catcher
    #    55       Wiggins         corner
    #    99       McCann          sniper
