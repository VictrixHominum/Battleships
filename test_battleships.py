import pytest
from battleships import *


def test_is_sunk1():
    assert is_sunk((2, 3, False, 3, {(2, 3), (2, 4), (2, 5)})) == True


def test_is_sunk2():
    assert is_sunk((5, 5, True, 5, {(5, 5), (6, 5), (8, 5), (9, 5)})) == False


def test_is_sunk3():
    assert is_sunk((0, 8, False, 2, {(0, 8), (0, 9)})) == True


def test_is_sunk4():
    assert is_sunk((4, 6, True, 4, {(4, 6), (5, 6), (6, 6), (7, 6)})) == True


def test_is_sunk5():
    assert is_sunk((6, 7, False, 3, {(6, 7), (6, 8)})) == False


def test_ship_type1():
    ship = (2, 3, True, 5, {})
    assert ship_type(ship) == "Battleship"


def test_ship_type2():
    ship = (4, 5, False, 4, {})
    assert ship_type(ship) == "Cruiser"


def test_ship_type3():
    ship = (9, 0, False, 3, {})
    assert ship_type(ship) == "Destroyer"


def test_ship_type4():
    ship = (1, 4, True, 2, {})
    assert ship_type(ship) == "Submarine"


def test_ship_type5():
    ship = (9, 3, True, 2, {})
    assert ship_type(ship) != "Cruiser"


def test_is_open_sea1():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}),
             (5, 6, False, 4, {}), (0, 7, True, 4, {}),
             (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert is_open_sea(0, 1, fleet) == False


def test_is_open_sea2():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}),
             (5, 6, False, 4, {}), (0, 7, True, 4, {}),
             (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert is_open_sea(2, 1, fleet) == True


def test_is_open_sea3():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}),
             (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert is_open_sea(9,2, fleet) == True


def test_is_open_sea4():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}),
             (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert is_open_sea(8, 4, fleet) == False


def test_is_open_sea5():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}),
             (5, 6, False, 4, {}), (0, 7, True, 4, {}),
             (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert is_open_sea(9, 0, fleet) == False


def test_ok_to_place_ship_at1():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 4, {}), (3, 6, True, 4, {}), (3, 9, True, 3, {}),
             (7, 3, False, 2, {}),
             (8, 7, True, 2, {})]
    assert ok_to_place_ship_at(3, 4, False, 3, fleet) == False
    # provide at least five tests in total for ok_to_place_ship_at by the project submission deadline


def test_place_ship_at1():
    fleet = [(2, 3, True, 3, {}), (1, 5, False, 4, {}), (3, 6, True, 4, {}), (3, 9, True, 3, {}), (7, 3, False, 2, {}),
             (8, 7, True, 2, {})]
    assert place_ship_at(0, 4, True, 5, fleet) == [(2, 3, True, 3, {}), (1, 5, False, 4, {}), (3, 6, True, 4, {}),
                                                   (3, 9, True, 3, {}),
                                                   (7, 3, False, 2, {}), (8, 7, True, 2, {}), (0, 4, True, 5, {})]
    # provide at least five tests in total for place_ship_at by the project submission deadline


def test_check_if_hits1():
    fleet = [(1, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 3, True, 3, {}),
             (1, 5, False, 4, {}), (3, 6, True, 4, {}),
             (3, 9, True, 3, {}), (7, 3, False, 2, {}), (8, 9, True, 2, {}), (8, 7, True, 2, {})]
    assert check_if_hits(9, 4, fleet) == True
    # provide at least five tests in total for check_if_hits by the project submission deadline


def test_hit1():
    fleet = [(1, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (2, 3, True, 3, {}),
             (1, 5, False, 4, {}), (3, 6, True, 4, {}),
             (3, 9, True, 3, {}), (7, 3, False, 2, {}), (8, 9, True, 2, {}), (8, 7, True, 2, {})]
    assert hit(0, 1, fleet) == (
        [(1, 3, True, 3, {}), (0, 0, False, 2, {(0, 1)}), (9, 1, False, 5, {}), (2, 3, True, 3, {}),
         (1, 5, False, 4, {}), (3, 6, True, 4, {}), (3, 9, True, 3, {}), (7, 3, False, 2, {}), (8, 9, True, 2, {}),
         (8, 7, True, 2, {})]
    )
    # provide at least five tests in total for hit by the project submission deadline


def test_are_unsunk_ships_left1():
    fleet = [(1, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 3, True, 3, {}),
             (3, 6, False, 4, {}), (3, 6, True, 4, {}),
             (3, 9, True, 3, {}), (7, 3, False, 2, {}), (8, 9, True, 2, {}), (8, 7, True, 2, {})]
    assert are_unsunk_ships_left(fleet) == True
    # provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
