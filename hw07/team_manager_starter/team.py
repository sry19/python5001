from player import Player


class Team:
    """A class representing a dodgeball team"""
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    def set_team_name(self, name):
        '''set the team name'''
        self.name = name

    def add_player(self, player_name, player_number, player_position):
        '''add a new player object to the team's players list'''
        new_player = Player(player_name, player_number, player_position)
        self.players.append(new_player)

    def cut_player(self, player_name):
        '''Remove the player with the name player_name
            from the players list'''
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                return

    def is_position_filled(self, position):
        '''checks whether there is currently at least one player on the team
            occupying the requested position'''
        for player in self.players:
            if player.position == position:
                return True
        return False

    def show_team_member(self):
        '''display (print to screen) the full team roster
            The lineup for Seattle Scorpions is:
            15       Garcia          catcher
            55       Wiggins         corner
            99       McCann          sniper
        '''
        print("The lineup for", self.name, "is:")
        if not self.players:
            print("The team currently has no players")
            return
        for player in self.players:
            print("{0:<4}  {1:<15}  {2:<11}".format(player.number,
                                                    player.name,
                                                    player.position))
