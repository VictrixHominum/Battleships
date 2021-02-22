Battleship is usually a two-player game, where each player has a fleet and an ocean (hidden from the other player), and tries to be the first to sink the other player's fleet. This is just a solo version, where the computer places the ships, and the human attempts to sink them.

The Ocean is a field of 10 x 10 squares. The squares are numbered from 0 to 9 in each dimension with numbers increasing from top to bottom and from left to right. 

To begin the game, the computer places all the 10 ships of the fleet in the ocean randomly. Each ship can be placed either horizontally (as shown in the figure above) or vertically. Moreover, no ships may be immediately adjacent to each other, either horizontally, vertically, or diagonally.

The human player does not know where the ships are. The human player tries to hit the ships, by calling out a row and column number. The computer responds with one bit of information--"You have a hit!" or "You missed!" (Note that the human player can call out the same location more than once, even though it does not make sense. If that happens, 2nd, 3rd, ... calls of the same location are misses.) When a ship is hit but not sunk, the program does  **not**  provide any information about what kind of a ship was hit. However, when a ship is hit  _and_  sinks, the program prints out a message  `"You sank a  _ship-type_!"`  

A ship is "sunk" when every square of the ship has been hit. Thus, it takes four hits (in four different places) to sink a battleship, three to sink a cruiser, two for a destroyer, and one for a submarine. The objective is to sink the fleet with as few shots as possible; the best possible score would be 20. (Low scores are better.) When all ships have been sunk, the program prints out a message that the game is over and tells how many shots were required.

The GUI version works in the same manner but instead of the player calling shots, the player clicks on square Minesweeper style.

## Data Structures

A ship by means of tuples

    (row, column, horizontal, length, hits)
where:

 - `row` and `column` are integers between 0 and 9 identifying, respectively, the row and column of the square of the top-left corner of the ship
 -  `horizontal` is a Boolean value equal to `True` if the ship is placed horizontally and `False` if placed vertically
 - `length` is an integer between 1 and 4 representing the length of the ship
 - `hits` is a set of tuples of the form `(row, column)` containing all the squares occupied by the ship that were hit
 
A fleet by means of a list

    [ship1, ship2, ....]
of ships.
