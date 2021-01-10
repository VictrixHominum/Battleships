import random
import re


def is_sunk(ship):
    """Checks to see if the length of the ship equals the number of hits, if so returns True, else False."""
    if len(ship[4]) == ship[3]:
        return True
    else:
        return False


def ship_type(ship):
    """Returns a ship's type by examining it's length element. If not a valid length returns 'Invalid'."""
    if ship[3] == 1:
        return "Submarine"
    elif ship[3] == 2:
        return "Destroyer"
    elif ship[3] == 3:
        return "Cruiser"
    elif ship[3] == 4:
        return "Battleship"
    else:
        return "Invalid"


def is_open_sea(row, column, fleet):
    """Adds all occupied and horizontally, vertically and diagonally adjacent co-ordinate pairs to a list. If the point
    selected is out of bounds or in the aforementioned list it returns False, else True."""

    # checks point is on the grid
    if 0 < (row or column) > 9:
        return False

    # creates list of all co-ordinates that are occupied or adjacent to the existing fleet
    blocked_spaces = []

    for ship in fleet:
        if ship[2] is True:
            [(blocked_spaces.append((ship[0], ship[1] + i))) for i in range(0, ship[3])]
        else:
            [(blocked_spaces.append((ship[0] + i, ship[1]))) for i in range(0, ship[3])]

    for i in range(len(blocked_spaces)):
        [blocked_spaces.append((blocked_spaces[i][0] + j, blocked_spaces[i][1] + k)) for k in range(-1, 2) for j in
         range(-1, 2)]

    blocked_spaces = set(blocked_spaces)

    # checks if point is in the non-valid point list
    if (row, column) in blocked_spaces:
        return False
    else:
        return True


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """Validates whether a ship can be placed in a given location. Checking that the fleet is not full, the ship is a
    valid ship, at no point would the ship exceed bounds and that the maximum number of this ship type has not been
     reached. If any of these conditions are met, it returns False, else True."""

    # checks to see if the fleet is full and new ship is a valid ship
    if (len(fleet) == 10) or (ship_type((row, column, horizontal, length)) == "Invalid") or horizontal and column + \
            length - 1 > 9 or not horizontal and row + length - 1 > 9:
        return False

    # checks if the number of ship of this type is already at the maximum
    count = 0
    for ship in fleet:
        if ship[3] == length:
            count += 1
    if count >= 6 - length:
        return False

    # checks if all points the ship would occupy are valid
    if horizontal is True:
        for j in range(0, length):
            if is_open_sea(row, column + j, fleet) is False:
                return False
    else:
        for j in range(0, length):
            if is_open_sea(row + j, column, fleet) is False:
                return False

    return True


def place_ship_at(row, column, horizontal, length, fleet):
    """If a ship has received a True from ok_to_place_ship_at() this adds it to the fleet."""
    if ok_to_place_ship_at(row, column, horizontal, length, fleet) is True:
        fleet.append((row, column, horizontal, length, set([])))
        return fleet

    else:
        return fleet


def randomly_place_all_ships():
    """Places all ships for a fleet. Starting by randomly generating a battleship and working its way down by length to
    submarine. For each ship it verifies placement is valid using ok_to_place_ship_at() allows ship to be added."""
    fleet = []

    for num in range(4, 0, -1):
        for count in range(0, 5 - num):
            finished = False
            while finished is not True:
                ship = (random.randint(0, 9), random.randint(0, 9), random.choice([True, False]), num)
                if ok_to_place_ship_at(ship[0], ship[1], ship[2], ship[3], fleet):
                    place_ship_at(ship[0], ship[1], ship[2], ship[3], fleet)
                    finished = True
    return fleet


def check_if_hits(row, column, fleet):
    """Creates a list of co-ordinate tuples that are occupied by a ship. If this point has already been hit or is not in
    this list it returns False, else True."""
    occupied_spaces = []
    for ship in fleet:
        if (row, column) in ship[4]:
            return False
        if ship[2] is True:
            [(occupied_spaces.append((ship[0], ship[1] + i))) for i in range(0, ship[3])]
        else:
            [(occupied_spaces.append((ship[0] + i, ship[1]))) for i in range(0, ship[3])]

    if (row, column) in occupied_spaces:
        return True
    else:
        return False


def hit(row, column, fleet):
    """If a co-ordinate returns a True from check_if_hits, this adds the hit to the ship in the fleet and returns the
    new fleet and ship hit."""
    if check_if_hits(row, column, fleet) is True:
        for x in range(len(fleet)):
            ship_points = []
            if fleet[x][2] is True:
                [(ship_points.append((fleet[x][0], fleet[x][1] + i))) for i in range(0, fleet[x][3])]
            else:
                [(ship_points.append((fleet[x][0] + i, fleet[x][1]))) for i in range(0, fleet[x][3])]
            if (row, column) in ship_points:
                fleet[x][4].add((row, column))
                fleet[x] = (fleet[x][0], fleet[x][1], fleet[x][2], fleet[x][3], fleet[x][4])
                return fleet, fleet[x]


def are_unsunk_ships_left(fleet):
    """For every ship in fleet it checks if sunk, if a ship is not sunk it returns True, else False"""
    for ship in fleet:
        if is_sunk(ship) is False:
            print("This ship is not sunk")
            return True
    print("All ships are sunk")
    return False


def main():
    """Main function: controls game flow."""

    # Initialises new randomly generate fleet
    current_fleet = randomly_place_all_ships()

    # Sets game variables
    error_message = "\n Please enter two integers between 0 and 9, separated with a space."
    game_over = False
    shots = 0

    print("\n Hello and welcome to Battleships! \n If at anypoint you wish to end the game simply enter 'Exit'. \n "
          "Good Luck!")

    while not game_over:
        loc_str = input("\n Enter a row and column to shoot at (separated by a space): ")

        # Checks that the player has not chosen to exit the game.
        if loc_str == 'Exit':
            return print("\n Game Over! You have exited the game after", shots, "shots.")

        # Checks that the input is valid.
        if re.match("^\s*[0-9]\s[0-9]\s*$", loc_str) is None:
            print("\n You did not enter two integers between 0 and 9." + error_message)
            continue

        # Turns input string into row and column integers for functions
        loc_str = [int(num) for num in loc_str.split()]
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1

        # If shot hits, affirms it and updates player. If a ship is sunk player is also updated. Confirms miss on miss.
        if check_if_hits(current_row, current_column, current_fleet):
            print("\n You hit!")
            current_fleet, ship_hit = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("\n You sank a " + ship_type(ship_hit) + "!")
        else:
            print("\n You missed!")

        # If all ships have been sunk, sets game_over to True, breaking the run loop and finishing the game.
        if not are_unsunk_ships_left(current_fleet):
            game_over = True

    print("\n Game over! You required", shots, "shots.")


if __name__ == '__main__':
    main()
