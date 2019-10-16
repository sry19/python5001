from team import Team
from bench import Bench


def main():
    print("Welcome to the team manager.")
    # Here's where we create objects for the team and the bench. These
    # objects will be able to call the methods we've defined in their
    # respective classes. When the constructor functions are called here,
    # the classes' __init__() method is called with these values
    # passed to it. In both of these cases no arguments are passed, here.
    # However, the `self` argument is always implicitly passed with any
    # method call.
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
            # TODO: call a function that calls
            # the appropriate method on the team
            # object to cut the player (you need
            # to write the function below)
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            # TODO: call a function to call the necessary
            # bench method to show the names of the players
            # who are currently on the bench.
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(team):
    name = input("What do you want to name the team?\n")
    while not check_team_name(name):
        name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def check_team_name(team_name):
    for letter in team_name:
        if (letter == ' ' or '0' <= letter <= '9' or 'a' <= letter <= 'z' or
           'A' <= letter <= 'Z'):
            continue
        else:
            return False
    return True


def do_show_team_roster(team):
    # TODO: call the method on the team object that
    # displays the roster
    team.show_team_member()


def do_check_position_filled(team):
    position = input("What position are you checking for?\n")
    # TODO: call the method on the team object that determines
    # whether a given position has at least one player filling it,
    # then print the appropriate message:
    # "Yes, the", position, "position is filled"
    # or
    # "No, the", position, "position is not filled"
    position = position.lower()
    while position not in ["catcher", "corner", "sniper", "thrower"]:
        position = input("What position are you checking for?\n")
        position = position.lower()
    if team.is_position_filled(position):
        print("Yes, the", position, "position is filled")
    else:
        print("No, the", position, "position is not filled")


def do_add_player_to_team(team):
    player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    while not player_number.isnumeric():
        player_number = input("What's " + player_name + "'s number?\n")
    player_position = input("What's " + player_name + "'s position?\n")
    player_position = player_position.lower()
    while player_position not in ["catcher", "corner", "sniper", "thrower"]:
        player_position = input("What's " + player_name + "'s position?\n")
        player_position = player_position.lower()
    # TODO: call the method on team that creates a new player and
    # adds the player to the team.
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_send_player_to_bench(team, bench):
    name = input("Who do you want to send to the bench?\n")
    # TODO: make sure that the player is actually on the team first,
    # and then call a method on the bench object to place the player
    # "on the bench". If this is accomplished successfully, print
    # "Sent", name, "to bench."
    # otherwise print
    # name, "isn't on the team."
    for player in team.players:
        if player.name == name:
            bench.send_to_bench(name)
            print("Sent", name, "to bench.")
            return
    print(name, "isn't on the team.")


def do_get_player_from_bench(bench):
    # TODO: get the best-rested player by name from the bench
    # (i.e. the player who has been on the bench longest). Print to
    # the screen the name of the player who was retrieved from the
    # bench. If the bench is empty, print to the screen that the
    # bench is empty.
    if not bench.players_on_bench:
        print("The bench is empty.")
    else:
        print("Got", bench.get_from_bench(), "from bench")


# TODO: write a function that calls the appropriate method on the team
# object to cut the player
def do_cut_player(team, bench):
    player_name = input("Who do you want to cut?\n")
    team.cut_player(player_name)
    bench.remove_from_bench(player_name)


# TODO: write a function to call the necessary method to show the
# names of the players who are currently on the bench.
def do_show_bench(bench):
    bench.display_bench()


def do_not_understand():
    print("I didn't understand that command")


main()
