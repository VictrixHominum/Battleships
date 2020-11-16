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
    ship = (9, 3, True, 1, {})
    assert ship_type(ship) == ""


def test_is_open_sea1():
    """Test to see if a valid location is rejected if in an occupied position"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}), (5, 6, False, 4, {}),
             (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert is_open_sea(0, 1, fleet) == False


def test_is_open_sea2():
    """Test to see if a valid location in an unoccupied or adjacent position is accepted"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}), (5, 6, False, 4, {}),
             (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert is_open_sea(2, 1, fleet) == True


def test_is_open_sea3():
    """Test to see if a invalid location in an unoccupied or adjacent position is rejected"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}),
             (6, 0, True, 2, {})]
    assert is_open_sea(10, 2, fleet) == False


def test_is_open_sea4():
    """Test to see if a valid location in an adjacent position is rejected"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}),
             (6, 0, True, 2, {})]
    assert is_open_sea(8, 4, fleet) == False


def test_is_open_sea5():
    """Test to see if a valid location in a diagonally adjacent position is rejected"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}), (5, 6, False, 4, {}),
             (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert is_open_sea(9, 0, fleet) == False


def test_ok_to_place_ship_at1():
    """Test to see if a valid ship, is rejected from placement at an intersecting location in a non-full fleet"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 3, {}), (0, 7, True, 4, {}), (1, 9, True, 3, {}),
             (7, 3, False, 2, {}), (7, 8, True, 2, {})]
    assert ok_to_place_ship_at(3, 4, False, 3, fleet) == False


def test_ok_to_place_ship_at2():
    """Test to see if a full fleet will reject a valid ship in a valid location"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}),
             (5, 6, False, 4, {}), (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}),
             (6, 0, True, 2, {})]
    assert ok_to_place_ship_at(3, 0, False, 2, fleet) == False


def test_ok_to_place_ship_at3():
    """Test to see if a valid ship that does not intersect and is not adjacent to any other ship is accepted to a
    non-full fleet"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 3, {}), (0, 7, True, 4, {}), (1, 9, True, 3, {}),
             (7, 3, False, 2, {})]
    assert ok_to_place_ship_at(7, 8, True, 2, fleet) == True


def test_ok_to_place_ship_at4():
    """Test to see if an invalid ship is rejected from a valid location"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 3, {}), (0, 7, True, 4, {}), (1, 9, True, 3, {}),
             (7, 3, False, 2, {}), (8, 7, True, 2, {})]
    assert ok_to_place_ship_at(9, 1, False, 6, fleet) == False


def test_ok_to_place_ship_at5():
    """Test to see if a valid ship that enters an invalid location is rejected"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 3, {}), (0, 7, True, 4, {}), (1, 9, True, 3, {}),
             (7, 3, False, 2, {})]
    assert ok_to_place_ship_at(7, 8, True, 4, fleet) == False


def test_place_ship_at1():
    """Test to see if a valid ship at a valid location is appended to the fleet list"""
    fleet = [(2, 3, True, 3, {}), (1, 5, False, 3, {}), (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}),
             (7, 8, True, 2, {})]
    assert place_ship_at(9, 1, False, 5, fleet) == [(2, 3, True, 3, {}), (1, 5, False, 4, {}), (0, 7, True, 4, {}),
                                                    (1, 9, True, 3, {}), (7, 3, False, 2, {}), (8, 7, True, 2, {}),
                                                    (9, 1, False, 5, {})]


def test_place_ship_at2():
    """Test to see if a ship at a valid location is not added to a full fleet"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}), (5, 6, False, 4, {}),
             (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert place_ship_at(3, 0, False, 2, fleet) == [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}),
                                                    (1, 5, True, 3, {}), (5, 6, False, 4, {}), (0, 7, True, 4, {}),
                                                    (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}),
                                                    (6, 0, True, 2, {})]


def test_place_ship_at3():
    """Test to see if an invalid ship at a valid location is not added to a non-full fleet"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 3, {}), (0, 7, True, 4, {}), (1, 9, True, 3, {}),
             (7, 3, False, 2, {})]
    assert place_ship_at(7, 8, True, 1, fleet) == [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 3, {}),
                                                   (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {})]


def test_place_ship_at4():
    """Test to see if a valid ship at an invalid location is not added to a non-full fleet"""
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 3, {}), (0, 7, True, 4, {}), (1, 9, True, 3, {}),
             (7, 3, False, 2, {}), (7, 8, True, 2, {})]
    assert place_ship_at(6, 8, True, 2, fleet) == [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 3, {}),
                                                   (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}),
                                                   (7, 8, True, 2, {})]


def test_place_ship_at5():
    """Test to see if a valid ship of a complete type (i.e. 2/2 cruisers have already been place) is not added to a
    non-full fleet """
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 3, {}), (0, 7, True, 4, {}), (1, 9, True, 3, {}),
             (7, 3, False, 2, {}), (7, 8, True, 2, {}), (5, 6, False, 4, {})]
    assert place_ship_at(9, 2, False, 4, fleet) == [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (1, 5, False, 3, {}),
                                                    (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}),
                                                    (7, 8, True, 2, {}), (5, 6, False, 4, {})]


def test_check_if_hits1():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}), (5, 6, False, 4, {}),
             (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert check_if_hits(9, 4, fleet) == True


def test_check_if_hits2():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}), (5, 6, False, 4, {}),
             (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert check_if_hits(3, 1, fleet) == False


def test_check_if_hits3():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}), (5, 6, False, 4, {}),
             (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert check_if_hits(6, 7, fleet) == False


def test_check_if_hits4():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}), (5, 6, False, 4, {}),
             (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert check_if_hits(3, 3, fleet) == True


def test_check_if_hits5():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}), (5, 6, False, 4, {}),
             (0, 7, True, 4, {}), (1, 9, True, 3, {}), (7, 3, False, 2, {}), (7, 8, True, 2, {}), (6, 0, True, 2, {})]
    assert check_if_hits(2, 9, fleet) == True


def test_hit1():
    fleet = [(2, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 5, True, 3, {}), (0, 7, True, 4, {}),
             (1, 9, True, 3, {}), (7, 3, False, 2, {}), (6, 0, True, 2, {}), (7, 8, True, 2, {}), (5, 6, False, 4, {})]
    assert hit(0, 1, fleet) == ([(2, 3, True, 3, {}), (0, 0, False, 2, {(0, 1)}), (9, 1, False, 5, {}),
                                 (1, 5, False, 4, {}), (3, 6, True, 4, {}), (3, 9, True, 3, {}), (7, 3, False, 2, {}),
                                 (8, 9, True, 2, {}), (8, 7, True, 2, {})], (0, 0, False, 2, {(0, 1)}))


def test_hit2():
    fleet = [(2, 3, True, 3, {(3, 3), (4, 3)}), (0, 0, False, 2, {(0, 1), (0, 2)}), (9, 1, False, 5, {(9, 5)}),
             (1, 5, True, 3, {(1, 5), (2, 5)}), (3, 6, True, 4, {(5, 6), (6, 6)}), (1, 9, True, 3, {}),
             (7, 3, False, 2, {(7, 3)}), (8, 9, True, 2, {(9, 9)}), (8, 7, True, 2, {})]
    assert hit(3, 5, fleet) == ([(2, 3, True, 3, {(3, 3), (4, 3)}), (0, 0, False, 2, {(0, 1), (0, 2)}),
                                (9, 1, False, 5, {(9, 5)}), (1, 5, True, 3, {(1, 5), (2, 5), (3, 5)}),
                                (3, 6, True, 4, {(5, 6), (6, 6)}), (1, 9, True, 3, {}), (7, 3, False, 2, {(7, 3)}),
                                (8, 9, True, 2, {(9, 9)}), (8, 7, True, 2, {})],
                                (1, 5, True, 3, {(1, 5), (2, 5), (3, 5)}))


def test_hit3():
    fleet = [(2, 3, True, 3, {(3, 3), (4, 3)}), (0, 0, False, 2, {(0, 1), (0, 2)}), (9, 1, False, 5, {(9, 5)}),
             (1, 5, True, 3, {(1, 5), (2, 5), (3, 5)}), (3, 6, True, 4, {(5, 6), (6, 6), (4, 6)}), (1, 9, True, 3, {}),
             (7, 3, False, 2, {(7, 3)}), (8, 9, True, 2, {(9, 9)}), (8, 7, True, 2, {})]
    assert hit(8, 9, fleet) == ([(2, 3, True, 3, {(3, 3), (4, 3)}), (0, 0, False, 2, {(0, 1), (0, 2)}),
                                 (9, 1, False, 5, {(9, 5)}), (1, 5, True, 3, {(1, 5), (2, 5), (3, 5)}),
                                 (3, 6, True, 4, {(5, 6), (6, 6), (4, 6)}), (1, 9, True, 3, {}),
                                 (7, 3, False, 2, {(7, 3)}), (8, 9, True, 2, {(9, 9), (8, 9)}), (8, 7, True, 2, {})],
                                (8, 9, True, 2, {(9, 9), (8, 9)}))


def test_hit4():
    fleet = [(2, 3, True, 3, {(3, 3), (4, 3)}), (0, 0, False, 2, {(0, 1), (0, 2)}),
             (9, 1, False, 5, {(9, 5), (9, 4), (9, 3), (9, 2), (9, 1)}), (1, 5, True, 3, {(1, 5), (2, 5), (3, 5)}),
             (3, 6, True, 4, {(5, 6), (6, 6), (4, 6), (3, 6)}), (1, 9, True, 3, {(2, 9), (1, 9)}),
             (7, 3, False, 2, {(7, 3), (7, 4)}), (8, 9, True, 2, {(9, 9), (8, 9)}), (8, 7, True, 2, {(8, 7)})]
    assert hit(9, 7, fleet) == ([(2, 3, True, 3, {(3, 3), (4, 3)}), (0, 0, False, 2, {(0, 1), (0, 2)}),
                                 (9, 1, False, 5, {(9, 5), (9, 4), (9, 3), (9, 2), (9, 1)}),
                                 (1, 5, True, 3, {(1, 5), (2, 5), (3, 5)}),
                                 (3, 6, True, 4, {(5, 6), (6, 6), (4, 6), (3, 6)}), (1, 9, True, 3, {(2, 9), (1, 9)}),
                                 (7, 3, False, 2, {(7, 3), (7, 4)}), (8, 9, True, 2, {(9, 9), (8, 9)}),
                                 (8, 7, True, 2, {(8, 7), (9, 7)})], (8, 7, True, 2, {(8, 7), (9, 7)}))


def test_hit5():
    fleet = [(2, 3, True, 3, {(3, 3), (4, 3)}), (0, 0, False, 2, {(0, 1), (0, 2)}),
             (9, 1, False, 5, {(9, 5), (9, 4), (9, 3), (9, 2), (9, 1)}), (1, 5, True, 3, {(1, 5), (2, 5), (3, 5)}),
             (3, 6, True, 4, {(5, 6), (6, 6), (4, 6), (3, 6)}), (1, 9, True, 3, {(2, 9), (1, 9)}),
             (7, 3, False, 2, {(7, 3), (7, 4)}), (8, 9, True, 2, {(9, 9), (8, 9)}), (8, 7, True, 2, {(8, 7), (9, 7)})]
    assert hit(3, 9, fleet) == ([(2, 3, True, 3, {(3, 3), (4, 3)}), (0, 0, False, 2, {(0, 1), (0, 2)}),
                                 (9, 1, False, 5, {(9, 5), (9, 4), (9, 3), (9, 2), (9, 1)}),
                                 (1, 5, True, 3, {(1, 5), (2, 5), (3, 5)}),
                                 (3, 6, True, 4, {(5, 6), (6, 6), (4, 6), (3, 6)}),
                                 (1, 9, True, 3, {(2, 9), (1, 9), (3, 9)}),
                                 (7, 3, False, 2, {(7, 3), (7, 4)}), (8, 9, True, 2, {(9, 9), (8, 9)}),
                                 (8, 7, True, 2, {(8, 7), (9, 7)})], (1, 9, True, 3, {(2, 9), (1, 9), (3, 9)}))



def test_are_unsunk_ships_left1():
    fleet = [(1, 3, True, 3, {}), (0, 0, False, 2, {}), (9, 1, False, 5, {}), (1, 3, True, 3, {}),
             (3, 6, False, 4, {}), (3, 6, True, 4, {}),
             (3, 9, True, 3, {}), (7, 3, False, 2, {}), (8, 9, True, 2, {}), (8, 7, True, 2, {})]
    assert are_unsunk_ships_left(fleet) == True
    # provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
