import random
import re


def is_sunk(ship):
    if len(ship[4]) == ship[3]:
        return True
    else:
        return False


def ship_type(ship):
    if ship[3] == 2:
        return "Submarine"
    elif ship[3] == 3:
        return "Destroyer"
    elif ship[3] == 4:
        return "Cruiser"
    elif ship[3] == 5:
        return "Battleship"
    else:
        return "Invalid"


def is_open_sea(row, column, fleet):
    # checks point is on the grid
    if 0 < (row or column) > 9:
        return False

    # creates list of all points that are occupied or adjacent to the existing fleet
    blocked_spaces = []

    for ship in fleet:
        if ship[2] == True:
            [(blocked_spaces.append((ship[0], ship[1] + i))) for i in range(0, ship[3])]
        else:
            [(blocked_spaces.append((ship[0] + i, ship[1]))) for i in range(0, ship[3])]

    for i in range(len(blocked_spaces)):
        blocked_spaces.append((blocked_spaces[i][0] + 1, blocked_spaces[i][1]))
        blocked_spaces.append((blocked_spaces[i][0] - 1, blocked_spaces[i][1]))
        blocked_spaces.append((blocked_spaces[i][0] + 1, blocked_spaces[i][1] + 1))
        blocked_spaces.append((blocked_spaces[i][0] + 1, blocked_spaces[i][1] - 1))
        blocked_spaces.append((blocked_spaces[i][0] - 1, blocked_spaces[i][1] + 1))
        blocked_spaces.append((blocked_spaces[i][0] - 1, blocked_spaces[i][1] - 1))
        blocked_spaces.append((blocked_spaces[i][0], blocked_spaces[i][1] + 1))
        blocked_spaces.append((blocked_spaces[i][0], blocked_spaces[i][1] - 1))

    blocked_spaces = set(blocked_spaces)

    # checks if point is in the non-valid point list
    if (row, column) in blocked_spaces:
        return False
    else:
        return True


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    allowed = True

    # checks to see if the fleet is full and new ship is a valid ship
    if (len(fleet) == 10) or (ship_type((row, column, horizontal, length)) == "Invalid"):
        return False

    # checks if the number of ship of this type is already at the maximum
    count = 0
    for ship in fleet:
        if ship[3] == length:
            count += 1
    if count >= 6 - length:
        return False

    # checks if all points the ship would occupy are valid
    for i in range(len(fleet)):
        if horizontal == True:
            for i in range(0, length):
                if is_open_sea(row, column + i, fleet) == False or column + (length - 1) > 9:
                    allowed = False

        else:
            for i in range(0, length):
                if is_open_sea(row + i, column, fleet) == False or row + (length - 1) > 9:
                    allowed = False

    if allowed is True:
        return True
    else:
        return False


def place_ship_at(row, column, horizontal, length, fleet):
    if ok_to_place_ship_at(row, column, horizontal, length, fleet) == True:
        fleet.append((row, column, horizontal, length, set([])))
        return fleet

    else:
        return fleet


def randomly_place_all_ships():
    fleet = []

    for num in range(5, 1, -1):
        for count in range(0, 6 - num):
            finished = False
            while finished is not True:
                ship = (random.randint(0, 9), random.randint(0, 9), random.choice([True, False]), num)
                if ok_to_place_ship_at(ship[0], ship[1], ship[2], ship[3], fleet):
                    place_ship_at(ship[0], ship[1], ship[2], ship[3], fleet)
                    finished = True

    return fleet


def check_if_hits(row, column, fleet):
    occupied_spaces = []
    for ship in fleet:
        if ship[2] == True:
            [(occupied_spaces.append((ship[0], ship[1] + i))) for i in range(0, ship[3])]
        else:
            [(occupied_spaces.append((ship[0] + i, ship[1]))) for i in range(0, ship[3])]

    if (row, column) in occupied_spaces:
        return True
    else:
        return False


def hit(row, column, fleet):
    if check_if_hits(row, column, fleet) == True:
        for x in range(len(fleet)):
            ship_points = []
            if fleet[x][2] == True:
                [(ship_points.append((fleet[x][0], fleet[x][1] + i))) for i in range(0, fleet[x][3])]
            else:
                [(ship_points.append((fleet[x][0] + i, fleet[x][1]))) for i in range(0, fleet[x][3])]
            if (row, column) in ship_points:
                fleet[x][4].add((row, column))
                fleet[x] = (fleet[x][0], fleet[x][1], fleet[x][2], fleet[x][3], fleet[x][4])
                return (fleet, fleet[x])



def are_unsunk_ships_left(fleet):
    for ship in fleet:
        if is_sunk(ship) == False:
            return True
    return False


def main():

    current_fleet = randomly_place_all_ships()

    print(current_fleet)

    error_message = "\n Please enter two integers between 0 and 9, separated with a space."
    game_over = False
    shots = 0

    print("\n Hello and welcome to Battleships! \n If at anypoint you wish to end the game simply enter 'Exit'. \n "
          "Good Luck!")

    while not game_over:
        loc_str = input("\n Enter a row and column to shoot at (separated by a space): ")

        if loc_str == 'Exit':
            return print("\n Game Over! You have exited the game after", shots, "shots.")

        if re.match("^\s*[0-9]\s[0-9]\s*$", loc_str) is None:
            print("\n You did not enter two integers between 0 and 9." + error_message)
            continue

        loc_str = [int(num) for num in loc_str.split()]

        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1

        if check_if_hits(current_row, current_column, current_fleet):
            print("\n You hit!")
            current_fleet, ship_hit = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("\n You sank a " + ship_type(ship_hit) + "!")
        else:
            print("\n You missed!")

        if not are_unsunk_ships_left(current_fleet):
            game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__':
    main()
