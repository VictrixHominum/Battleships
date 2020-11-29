import pytest
from battleships import *


def test_is_sunk1():
    assert is_sunk((2, 3, True, 3, {(2, 3), (2, 4), (2, 5)})) == True


def test_is_sunk2():
    assert is_sunk((5, 5, True, 4, {(5, 5), (6, 5), (8, 5)})) == False


def test_is_sunk3():
    assert is_sunk((0, 8, True, 2, {(0, 8), (0, 9)})) == True


def test_is_sunk4():
    assert is_sunk((4, 6, False, 3, {(4, 6), (5, 6), (6, 6)})) == True


def test_is_sunk5():
    assert is_sunk((6, 7, True, 1, {})) == False


def test_ship_type1():
    ship = (2, 3, False, 4, set([]))
    assert ship_type(ship) == "Battleship"


def test_ship_type2():
    ship = (4, 5, True, 3, set([]))
    assert ship_type(ship) == "Cruiser"


def test_ship_type3():
    ship = (9, 0, True, 2, set([]))
    assert ship_type(ship) == "Destroyer"


def test_ship_type4():
    ship = (1, 4, False, 1, set([]))
    assert ship_type(ship) == "Submarine"


def test_ship_type5():
    ship = (9, 3, False, 0, set([]))
    assert ship_type(ship) == "Invalid"


def test_is_open_sea1():
    """Test to see if a valid location is rejected if in an occupied position"""
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 5, False, 2, set([])), (5, 6, True, 3, set([])),
             (0, 7, False, 3, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])), (6, 0, False, 1, set([]))]
    assert is_open_sea(0, 1, fleet) == False


def test_is_open_sea2():
    """Test to see if a valid location in an unoccupied or adjacent position is accepted"""
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 5, False, 2, set([])), (5, 6, True, 3, set([])),
             (0, 7, False, 3, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])), (6, 0, False, 1, set([]))]
    assert is_open_sea(2, 1, fleet) == True


def test_is_open_sea3():
    """Test to see if a invalid location in an unoccupied or adjacent position is rejected"""
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])),
             (6, 0, False, 1, set([]))]
    assert is_open_sea(10, 2, fleet) == False


def test_is_open_sea4():
    """Test to see if a valid location in an adjacent position is rejected"""
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])),
             (6, 0, False, 1, set([]))]
    assert is_open_sea(1, 0, fleet) == False


def test_is_open_sea5():
    """Test to see if a valid location in a diagonally adjacent position is rejected"""
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 5, False, 2, set([])), (5, 6, True, 3, set([])),
             (0, 7, False, 3, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])), (6, 0, False, 1, set([]))]
    assert is_open_sea(9, 0, fleet) == False


def test_ok_to_place_ship_at1():
    """Test to see if a valid ship, is rejected from placement at an intersecting location in a non-full fleet"""
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (1, 5, True, 2, set([])), (0, 7, False, 3, set([])), (1, 9, False, 2, set([])),
             (7, 3, True, 1, set([])), (7, 8, False, 1, set([]))]
    assert ok_to_place_ship_at(3, 4, True, 3, fleet) == False


def test_ok_to_place_ship_at2():
    """Test to see if a full fleet will reject a valid ship in a valid location"""
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 5, False, 2, set([])),
             (5, 6, True, 3, set([])), (0, 7, False, 3, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])),
             (6, 0, False, 1, set([]))]
    assert ok_to_place_ship_at(3, 0, True, 1, fleet) == False


def test_ok_to_place_ship_at3():
    """Test to see if a valid ship that does not intersect and is not adjacent to any other ship is accepted to a
    non-full fleet"""
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (1, 5, True, 2, set([])), (0, 7, False, 3, set([])), (1, 9, False, 2, set([])),
             (7, 3, True, 1, set([]))]
    assert ok_to_place_ship_at(7, 8, False, 1, fleet) == True


def test_ok_to_place_ship_at4():
    """Test to see if an invalid ship is rejected from a valid location"""
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (1, 5, True, 2, set([])), (0, 7, False, 3, set([])), (1, 9, False, 2, set([])),
             (7, 3, True, 1, set([])), (8, 7, False, 1, set([]))]
    assert ok_to_place_ship_at(9, 1, True, 5, fleet) == False


def test_ok_to_place_ship_at5():
    """Test to see if a valid ship that enters an invalid location is rejected"""
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (1, 5, True, 2, set([])), (1, 0, False, 3, set([])), (1, 9, False, 2, set([])),
             (7, 3, True, 1, set([]))]
    assert ok_to_place_ship_at(7, 8, False, 4, fleet) == False


def test_place_ship_at1():
    """Test to see if a valid ship at a valid location is appended to the fleet list"""
    fleet = [(2, 3, False, 2, set([])), (0, 5, True, 1, set([])), (7, 0, True, 3, set([])), (9, 1, True, 2, set([])), (3, 7, True, 1, set([])),
             (8, 7, False, 1, set([]))]
    assert place_ship_at(5, 5, True, 3, fleet) == [(2, 3, False, 2, set([])), (0, 5, True, 1, set([])), (7, 0, True, 3, set([])),
                                                   (9, 1, True, 2, set([])), (3, 7, True, 1, set([])), (8, 7, False, 1, set([])),
                                                   (5, 5, True, 3, set([]))]


def test_place_ship_at2():
    """Test to see if a ship at a valid location is not added to a full fleet"""
    fleet = [(2, 3, False, 2, set([])), (0, 5, True, 1, set([])), (1, 9, True, 4, set([])), (5, 1, True, 2, set([])), (5, 5, True, 3, set([])),
             (1, 0, False, 3, set([])), (1, 9, False, 2, set([])), (6, 3, True, 1, set([])), (8, 7, False, 1, set([])), (3, 7, False, 1, set([]))]
    assert place_ship_at(3, 0, False, 1, fleet) == [(2, 3, False, 2, set([])), (0, 5, True, 1, set([])), (1, 9, True, 4, set([])),
                                                    (5, 1, True, 2, set([])), (5, 5, True, 3, set([])), (1, 0, False, 3, set([])),
                                                    (1, 9, False, 2, set([])), (6, 3, True, 1, set([])), (8, 7, False, 1, set([])),
                                                    (3, 7, False, 1, set([]))]


def test_place_ship_at3():
    """Test to see if an invalid ship at a valid location is not added to a non-full fleet"""
    fleet = [(2, 3, False, 2, set([])), (0, 5, True, 1, set([])), (1, 9, True, 4, set([])), (5, 1, True, 2, set([])), (5, 5, True, 3, set([])),
             (1, 0, False, 3, set([])), (1, 9, False, 2, set([])), (6, 3, True, 1, set([]))]
    assert place_ship_at(0, 7, True, 0, fleet) == [(2, 3, False, 2, set([])), (0, 5, True, 1, set([])), (1, 9, True, 4, set([])),
                                                   (5, 1, True, 2, set([])), (5, 5, True, 3, set([])), (1, 0, False, 3, set([])),
                                                   (1, 9, False, 2, set([])), (6, 3, True, 1, set([]))]


def test_place_ship_at4():
    """Test to see if a valid ship at an invalid location is not added to a non-full fleet"""
    fleet = [(2, 3, False, 2, set([])), (0, 5, True, 1, set([])), (1, 9, True, 4, set([])), (5, 1, True, 2, set([])), (5, 5, True, 3, set([])),
             (1, 0, False, 3, set([])), (1, 9, False, 2, set([])), (6, 3, True, 1, set([]))]
    assert place_ship_at(10, 9, True, 1, fleet) == [(2, 3, False, 2, set([])), (0, 5, True, 1, set([])), (1, 9, True, 4, set([])),
                                                   (5, 1, True, 2, set([])), (5, 5, True, 3, set([])), (1, 0, False, 3, set([])),
                                                   (1, 9, False, 2, set([])), (6, 3, True, 1, set([]))]


def test_place_ship_at5():
    """Test to see if a valid ship of a complete type (i.e. 2/2 cruisers have already been place) is not added to a
    non-full fleet """
    fleet = [(2, 3, False, 2, set([])), (0, 5, True, 1, set([])), (1, 9, True, 4, set([])), (5, 1, True, 2, set([])), (5, 5, True, 3, set([])),
             (1, 0, False, 3, set([])), (1, 9, False, 2, set([])), (6, 3, True, 1, set([]))]
    assert place_ship_at(3, 7, False, 2, fleet) == [(2, 3, False, 2, set([])), (0, 5, True, 1, set([])), (1, 9, True, 4, set([])),
                                                    (5, 1, True, 2, set([])), (5, 5, True, 3, set([])), (1, 0, False, 3, set([])),
                                                    (1, 9, False, 2, set([])), (6, 3, True, 1, set([]))]


def test_check_if_hits1():
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 5, False, 2, set([])), (5, 6, True, 3, set([])),
             (0, 7, False, 3, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])), (6, 0, False, 1, set([]))]
    assert check_if_hits(9, 4, fleet) == True


def test_check_if_hits2():
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 5, False, 2, set([])), (5, 6, True, 3, set([])),
             (0, 7, False, 3, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])), (6, 0, False, 1, set([]))]
    assert check_if_hits(3, 1, fleet) == False


def test_check_if_hits3():
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 5, False, 2, set([])), (5, 6, True, 3, set([])),
             (0, 7, False, 3, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])), (6, 0, False, 1, set([]))]
    assert check_if_hits(6, 7, fleet) == False


def test_check_if_hits4():
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 5, False, 2, set([])), (5, 6, True, 3, set([])),
             (0, 7, False, 3, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])), (6, 0, False, 1, set([]))]
    assert check_if_hits(3, 3, fleet) == True


def test_check_if_hits5():
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 5, False, 2, set([])), (5, 6, True, 3, set([])),
             (0, 7, False, 3, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (7, 8, False, 1, set([])), (6, 0, False, 1, set([]))]
    assert check_if_hits(2, 9, fleet) == True


def test_hit1():
    fleet = [(2, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 5, False, 2, set([])), (3, 6, False, 3, set([])),
             (1, 9, False, 2, set([])), (7, 3, True, 1, set([])), (6, 0, False, 1, set([])), (7, 8, False, 1, set([])), (5, 6, True, 3, set([]))]
    assert hit(0, 0, fleet) == ([(2, 3, False, 2, set([])), (0, 0, True, 1, {(0, 0)}), (9, 1, True, 4, set([])),
                                 (1, 5, False, 2, set([])), (3, 6, False, 3, set([])), (1, 9, False, 2, set([])), (7, 3, True, 1, set([])),
                                 (6, 0, False, 1, set([])), (7, 8, False, 1, set([])),  (5, 6, True, 3, set([]))], (0, 0, True, 1, {(0, 0)}))


def test_hit2():
    fleet = [(2, 3, False, 2, {(2, 3), (3, 3)}), (0, 0, True, 1, {(0, 0)}), (9, 1, True, 4, {(9, 4)}),
             (1, 5, False, 2, {(1, 5)}), (3, 6, False, 3, {(4, 6), (5, 6)}), (1, 9, False, 2, set([])),
             (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, {(8, 9)}), (8, 7, False, 1, set([]))]
    assert hit(2, 5, fleet) == ([(2, 3, False, 2, {(2, 3), (3, 3)}), (0, 0, True, 1, {(0, 0)}),
                                (9, 1, True, 4, {(9, 4)}), (1, 5, False, 2, {(1, 5), (2, 5)}),
                                (3, 6, False, 3, {(4, 6), (5, 6)}), (1, 9, False, 2, set([])), (7, 3, True, 1, {(7, 3)}),
                                (8, 9, False, 1, {(8, 9)}), (8, 7, False, 1, set([]))],
                                (1, 5, False, 2, {(1, 5), (2, 5)}))


def test_hit3():
    fleet = [(2, 3, False, 2, {(2, 3), (3, 3)}), (0, 0, True, 1, {(0, 0)}), (9, 1, True, 4, {(9, 4)}),
             (1, 5, False, 2, {(1, 5), (2, 5)}), (3, 6, False, 3, {(5, 6), (3, 6), (4, 6)}), (1, 9, False, 2, set([])),
             (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, set([])), (8, 7, False, 1, set([]))]
    assert hit(8, 9, fleet) == ([(2, 3, False, 2, {(2, 3), (3, 3)}), (0, 0, True, 1, {(0, 0)}),
                                 (9, 1, True, 4, {(9, 4)}), (1, 5, False, 2, {(1, 5), (2, 5)}),
                                 (3, 6, False, 3, {(5, 6), (3, 6), (4, 6)}), (1, 9, False, 2, set([])),
                                 (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, {(8, 9)}), (8, 7, False, 1, set([]))],
                                (8, 9, False, 1, {(8, 9)}))


def test_hit4():
    fleet = [(2, 3, False, 2, {(2, 3), (3, 3)}), (0, 0, True, 1, {(0, 0)}),
             (9, 1, True, 4, {(9, 4), (9, 3), (9, 2), (9, 1)}), (1, 5, False, 2, {(1, 5), (2, 5)}),
             (3, 6, False, 3, {(5, 6), (3, 6)}), (1, 9, False, 2, {(2, 9), (1, 9)}),
             (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, {(8, 9)}), (8, 7, False, 1, {(8, 7)})]
    assert hit(4, 6, fleet) == ([(2, 3, False, 2, {(2, 3), (3, 3)}), (0, 0, True, 1, {(0, 0)}),
                                 (9, 1, True, 4, {(9, 4), (9, 3), (9, 2), (9, 1)}),
                                 (1, 5, False, 2, {(1, 5), (2, 5)}),
                                 (3, 6, False, 3, {(5, 6), (3, 6), (4, 6)}), (1, 9, False, 2, {(2, 9), (1, 9)}),
                                 (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, {(8, 9)}),
                                 (8, 7, False, 1, {(8, 7)})], (3, 6, False, 3, {(5, 6), (3, 6), (4, 6)}))


def test_hit5():
    fleet = [(2, 3, False, 2, {(2, 3), (3, 3)}), (0, 0, True, 1, {(0, 0)}),
             (9, 1, True, 4, {(9, 4), (9, 3), (9, 2), (9, 1)}), (1, 5, False, 2, {(1, 5), (2, 5)}),
             (3, 6, False, 3, {(5, 6), (4, 6), (3, 6)}), (1, 9, False, 2, {(1, 9)}),
             (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, {(8, 9)}), (8, 7, False, 1, {(8, 7)})]
    assert hit(2, 9, fleet) == ([(2, 3, False, 2, {(2, 3), (3, 3)}), (0, 0, True, 1, {(0, 0)}),
                                 (9, 1, True, 4, {(9, 4), (9, 3), (9, 2), (9, 1)}),
                                 (1, 5, False, 2, {(1, 5), (2, 5)}),
                                 (3, 6, False, 3, {(5, 6), (4, 6), (3, 6)}),
                                 (1, 9, False, 2, {(1, 9), (2, 9)}),
                                 (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, {(8, 9)}),
                                 (8, 7, False, 1, {(8, 7)})], (1, 9, False, 2, {(1, 9), (2, 9)}))


def test_are_unsunk_ships_left1():
    fleet = [(1, 3, False, 2, set([])), (0, 0, True, 1, set([])), (9, 1, True, 4, set([])), (1, 3, False, 2, set([])),
             (3, 6, True, 3, set([])), (3, 6, False, 3, set([])), (3, 9, False, 2, set([])), (7, 3, True, 1, set([])), (8, 9, False, 1, set([])),
             (8, 7, False, 1, set([]))]
    assert are_unsunk_ships_left(fleet) == True


def test_are_unsunk_ships_left2():
    fleet = [(2, 3, False, 2, {(3, 3), (2, 3)}), (0, 0, True, 1, {(0, 0)}),
             (9, 1, True, 4, {(9, 4), (9, 3), (9, 2), (9, 1)}), (1, 5, False, 2, {(1, 5), (2, 5)}),
             (3, 6, False, 3, {(5, 6), (4, 6), (3, 6)}), (1, 9, False, 2, {(2, 9), (1, 9)}),
             (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, {(8, 9)}), (8, 7, False, 1, {(8, 7)})]
    assert are_unsunk_ships_left(fleet) == False


def test_are_unsunk_ships_left3():
    fleet = [(2, 3, False, 2, {(3, 3), (2, 3)}), (0, 0, True, 1, {(0, 0)}),
             (9, 1, True, 4, {(9, 3), (9, 2), (9, 1)}), (1, 5, False, 2, {(1, 5), (2, 5)}),
             (3, 6, False, 3, {(5, 6), (4, 6), (3, 6)}), (1, 9, False, 2, {(2, 9), (1, 9)}),
             (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, {(8, 9)}), (8, 7, False, 1, {(8, 7)})]
    assert are_unsunk_ships_left(fleet) == True


def test_are_unsunk_ships_left4():
    fleet = [(2, 3, False, 2, {(3, 3), (2, 3)}), (0, 0, True, 1, {(0, 0)}), (9, 1, True, 4, {(9, 4)}),
             (1, 5, False, 2, {(1, 5), (2, 5)}), (3, 6, False, 3, {(5, 6), (4, 6)}), (1, 9, False, 2, set([])),
             (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, {(8, 9)}), (8, 7, False, 1, set([]))]
    assert are_unsunk_ships_left(fleet) == True


def test_are_unsunk_ships_left5():
    fleet = [(2, 3, False, 2, {(3, 3), (2, 3)}), (0, 0, True, 1, {(0, 0)}),
             (9, 1, True, 4, {(9, 4), (9, 3), (9, 2), (9, 1)}), (1, 5, False, 2, {(1, 5), (2, 5)}),
             (3, 6, False, 3, {(5, 6), (4, 6), (3, 6)}), (1, 9, False, 2, {(1, 9)}),
             (7, 3, True, 1, {(7, 3)}), (8, 9, False, 1, {(8, 9)}), (8, 7, False, 1, {(8, 7)})]
    assert are_unsunk_ships_left(fleet) == True
