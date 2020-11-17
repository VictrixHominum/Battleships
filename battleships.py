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
    if 0 < (row or column) > 9:
        return False

    blocked_spaces = []

    for ship in fleet:
        blocked_spaces.append((ship[0], ship[1]))
        if ship[2] == True:
            [(blocked_spaces.append((ship[0] + i, ship[1]))) for i in range(1, ship[3])]
        else:
            [(blocked_spaces.append((ship[0], ship[1] + i))) for i in range(1, ship[3])]

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

    if (row, column) in blocked_spaces:
        return False
    else:
        return True


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    if (len(fleet) == 10) or (ship_type((row, column, horizontal, length)) == "Invalid"):
        return False

    if horizontal == True:
        for i in range(0, length):
            if is_open_sea(row, column + i, fleet) == False or column + (length-1) > 9:
                return False
            else:
                return True
    else:
        for i in range(0, length):
            if is_open_sea(row + i, column, fleet) == False or row + (length-1) > 9:
                return False
            else:
                return True



"""def place_ship_at(row, column, horizontal, length, fleet):
    #remove pass and add your implementation
    pass

def randomly_place_all_ships():
    #remove pass and add your implementation
    pass

def check_if_hits(row, column, fleet):
    #remove pass and add your implementation
    pass

def hit(row, column, fleet):
    #remove pass and add your implementation
    pass

def are_unsunk_ships_left(fleet):
    #remove pass and add your implementation
    pass

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()    
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_shis_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main() """
