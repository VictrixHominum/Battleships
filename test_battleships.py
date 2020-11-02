import pytest
from battleships import *

def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    #add at least four more tests for is_sunk by the project submission deadline

def test_ship_type1():
    ship = "battleship"
    assert ship_type == True

def test_ship_type2():
    ship = "cruiser"
    assert ship_type(ship) == True

def test_ship_type3():
    ship = "destroyer"
    assert ship_type(ship) == True

def test_ship_type4():
    ship = "submarine"
    assert ship_type(ship) == True
    #provide at least five tests in total for ship_type by the project submission deadline

def test_is_open_sea1():
    fleet = "player"
    assert is_open_sea(2,3,fleet) == True
    #add at least one test for open_sea by the deadline of session 7 assignment
    #provide at least five tests in total for open_sea by the project submission deadline

def test_ok_to_place_ship_at1():
    #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

def test_place_ship_at1():
    #add at least one test for place_ship_at by the deadline of session 7 assignment
    #provide at least five tests in total for place_ship_at by the project submission deadline

def test_check_if_hits1():
    #add at least one test for check_if_hits by the deadline of session 7 assignment
    #provide at least five tests in total for check_if_hits by the project submission deadline

def test_hit1():
    #add at least one test for hit by the deadline of session 7 assignment
    #provide at least five tests in total for hit by the project submission deadline

def test_are_unsunk_ships_left1():
    #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    
