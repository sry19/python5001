# Author: Ruoyun Sun
# The program manages teams. The system enables the user to set the name of
# the team, check on the status of the team, and to manage the players on the
# team in various ways.
from team import Team
from bench import Bench


def main():
    '''manage the input
        None -> None'''
    print("Welcome to the team manager.")
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(team):
    '''give a name to the team
        team object -> None'''
    name = input("What do you want to name the team?\n")
    while not check_team_name(name):
        name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def check_team_name(team_name):
    '''check if the team name only has number, letter or whitespace
            string -> Boolean'''
    for letter in team_name:
        if (letter == ' ' or '0' <= letter <= '9' or 'a' <= letter <= 'z' or
           'A' <= letter <= 'Z'):
            continue
        else:
            return False
    return True


def do_show_team_roster(team):
    '''displays the team roster
        team object -> None'''
    team.show_team_member()


def do_check_position_filled(team):
    '''call the method on the team object that determines
        whether a given position has at least one player filling it
        team object -> None'''
    position = input("What position are you checking for?\n")
    position = position.lower()
    while position not in ["catcher", "corner", "sniper", "thrower"]:
        position = input("What position are you checking for?\n")
        position = position.lower()
    if team.is_position_filled(position):
        print("Yes, the", position, "position is filled")
    else:
        print("No, the", position, "position is not filled")


def do_add_player_to_team(team):
    '''use name, number and position to add a new player to team
        team object -> None'''
    player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    while not player_number.isnumeric():
        player_number = input("What's " + player_name + "'s number?\n")
    player_position = input("What's " + player_name + "'s position?\n")
    player_position = player_position.lower()
    while player_position not in ["catcher", "corner", "sniper", "thrower"]:
        player_position = input("What's " + player_name + "'s position?\n")
        player_position = player_position.lower()
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_send_player_to_bench(team, bench):
    '''if a player is in the team, we can send it to the bench, else
            print 'XX isn't on the team'
            team object, bench object -> None'''
    name = input("Who do you want to send to the bench?\n")
    for player in team.players:
        if player.name == name:
            bench.send_to_bench(name)
            print("Sent", name, "to bench.")
            return
    print(name, "isn't on the team.")


def do_get_player_from_bench(bench):
    '''get and delete a player in the bench(FIFO), then print his name
            bench object -> None'''
    if not bench.players_on_bench:
        print("The bench is empty.")
    else:
        print("Got", bench.get_from_bench(), "from bench")


def do_cut_player(team, bench):
    '''cut a player from the team, also cut the player if he is on the bench
        team object, bench object -> None'''
    player_name = input("Who do you want to cut?\n")
    team.cut_player(player_name)
    bench.remove_from_bench(player_name)


def do_show_bench(bench):
    '''show players on the bench
        bench object -> None'''
    bench.display_bench()


def do_not_understand():
    '''when input is meaningless
            None -> None'''
    print("I didn't understand that command")


main()
