import pytest
from battleships import *


def test_is_sunk1():
    s = (2, 3, False, 3, {(2, 3), (3, 3), (4, 3)})
    assert is_sunk(s) == True
    # add at least four more tests for is_sunk by the project submission deadline


def test_ship_type1():
    ship = (2, 3, True, 5, {})
    assert ship_type(ship) == "Battleship"


def test_ship_type2():
    ship = (4, 5, False, 4, {})
    assert ship_type(ship) == "Cruiser"


def test_ship_type3():
    ship = (10, 1, False, 3, {})
    assert ship_type(ship) == "Destroyer"


def test_ship_type4():
    ship = (1, 4, True, 2, {})
    assert ship_type(ship) == "Submarine"


def test_ship_type5():
    ship = (10, 3, True, 1, {})
    assert ship_type(ship) != "Cruiser"
    # provide at least five tests in total for ship_type by the project submission deadline


def test_is_open_sea1():
    fleet = [(3, 4, True, 3, {}), (1, 1, False, 2, {}), (10, 2, False, 5, {}), (2, 4, True, 3, {}),
             (2, 6, False, 4, {}), (4, 7, True, 4, {}),
             (4, 10, True, 3, {}), (8, 4, False, 2, {}), (9, 10, True, 2, {}), (9, 8, True, 2, {})]
    assert is_open_sea(2, 3, fleet) == False
    # provide at least five tests in total for open_sea by the project submission deadline


def test_ok_to_place_ship_at1():
    fleet = [(3, 4, True, 3, {}), (1, 1, False, 2, {}), (2, 6, False, 4, {}), (4, 7, True, 4, {}), (4, 10, True, 3, {}),
             (8, 4, False, 2, {}),
             (9, 8, True, 2, {})]
    assert ok_to_place_ship_at(4, 5, False, 3, fleet) == False
    # provide at least five tests in total for ok_to_place_ship_at by the project submission deadline


def test_place_ship_at1():
    fleet = [(3, 4, True, 3, {}), (2, 6, False, 4, {}), (4, 7, True, 4, {}), (4, 10, True, 3, {}), (8, 4, False, 2, {}),
             (9, 8, True, 2, {})]
    assert place_ship_at(1, 5, True, 5, fleet) == [(3, 4, True, 3, {}), (2, 6, False, 4, {}), (4, 7, True, 4, {}),
                                                   (4, 10, True, 3, {}),
                                                   (8, 4, False, 2, {}), (9, 8, True, 2, {}), (1, 5, True, 5, {})]
    # provide at least five tests in total for place_ship_at by the project submission deadline


def test_check_if_hits1():
    fleet = [(2, 4, True, 3, {}), (1, 1, False, 2, {}), (10, 2, False, 5, {}), (2, 4, True, 3, {}),
             (2, 6, False, 4, {}), (4, 7, True, 4, {}),
             (4, 10, True, 3, {}), (8, 4, False, 2, {}), (9, 10, True, 2, {}), (9, 8, True, 2, {})]
    assert check_if_hits(10, 5, fleet) == True
    # provide at least five tests in total for check_if_hits by the project submission deadline


def test_hit1():
    fleet = [(2, 4, True, 3, {}), (1, 1, False, 2, {}), (10, 2, False, 5, {}), (3, 4, True, 3, {}),
             (2, 6, False, 4, {}), (4, 7, True, 4, {}),
             (4, 10, True, 3, {}), (8, 4, False, 2, {}), (9, 10, True, 2, {}), (9, 8, True, 2, {})]
    assert hit(1, 2, fleet) == (
        [(2, 4, True, 3, {}), (1, 1, False, 2, {(1, 2)}), (10, 2, False, 5, {}), (3, 4, True, 3, {}),
         (2, 6, False, 4, {}), (4, 7, True, 4, {}), (4, 10, True, 3, {}), (8, 4, False, 2, {}), (9, 10, True, 2, {}),
         (9, 8, True, 2, {})], (1, 1, False, 2, {(1, 2)})
    )
    # provide at least five tests in total for hit by the project submission deadline


def test_are_unsunk_ships_left1():
    fleet = [(2, 4, True, 3, {}), (1, 1, False, 2, {}), (10, 2, False, 5, {}), (2, 4, True, 3, {}),
             (2, 7, False, 4, {}), (4, 7, True, 4, {}),
             (4, 10, True, 3, {}), (8, 4, False, 2, {}), (9, 10, True, 2, {}), (9, 8, True, 2, {})]
    assert are_unsunk_ships_left(fleet) == True
    # provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
