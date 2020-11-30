from tkinter import *
from tkinter.messagebox import *
from battleships import *

rows = 11
cols = 11
buttons = []
field = []
current_fleet = randomly_place_all_ships()
shots = 0
hits = 0



def click_on(x, y):
    """Create Response to button click depending if the co-ordinate has been hit or not"""
    global buttons, field, rows, cols, current_fleet, shots, hits

    shots += 1
    if field[x][y] == 0:
        buttons[x][y]["text"] = " "
    buttons[x][y]['state'] = 'disabled'
    if check_if_hits(x-1, y-1, current_fleet) is True:
        current_fleet, ship_hit = hit(x-1, y-1, current_fleet)
        hits += 1
        buttons[x][y].config(relief=SUNKEN, bg='#FF0000')
        if is_sunk(ship_hit) is True:
            co_ords = list(ship_hit[4])
            for (x, y) in co_ords:
                if ship_type(ship_hit) == "Submarine":
                    buttons[x+1][y+1].config(text="S")
                elif ship_type(ship_hit) == "Destroyer":
                    buttons[x+1][y+1].config(text="D")
                elif ship_type(ship_hit) == "Cruiser":
                    buttons[x+1][y+1].config(text="C")
                elif ship_type(ship_hit) == "Battleship":
                    buttons[x + 1][y + 1].config(text="B")
    else:
        buttons[x][y].config(relief=SUNKEN, bg='#0000CD')

    if are_unsunk_ships_left(current_fleet) is False:
        showinfo("Game Over", f" You have won! \n You took {shots} shots.")
        for x in range(0, rows):
            for y in range(0, cols):
                buttons[x][y]['state'] = 'disabled'


class Battleships:

    def __init__(self, master):
        global rows, cols, buttons, field
        self.master = master
        master.title("Battleships")

        '''Create Menu with options'''
        menu_bar = Menu(master)
        menu_bar.add_command(label="Exit", command=lambda: master.destroy())
        menu_bar.add_command(label="Restart", command=lambda: self.restart())
        master.config(menu=menu_bar)

        '''Build button grid with co-ordinate reference'''
        self.label = Label(master, text="Battleships")
        self.label.grid(row=0, column=0, columnspan=11, sticky=W + E)

        field = []
        for x in range(0, rows):
            field.append([])
            for y in range(0, cols):
                field[x].append(0)

        buttons = []
        for x in range(0, rows):
            buttons.append([])
            for y in range(0, cols):
                if x == 0:
                    l = Label(master, text=str(x))
                    buttons[x].append(l)
                elif y == 0:
                    l = Label(master, text=str(y))
                    buttons[x].append(l)
                else:
                    b = Button(master, text=" ", width=2, command=lambda x=x, y=y: click_on(x, y))
                    b.grid(row=x + 1, column=y, sticky=N + W + S + E)
                    buttons[x].append(b)

        self.y0 = Label(master, text="0")
        self.y0.grid(row=2, column=0)
        self.y1 = Label(master, text="1")
        self.y1.grid(row=3, column=0)
        self.y2 = Label(master, text="2")
        self.y2.grid(row=4, column=0)
        self.y3 = Label(master, text="3")
        self.y3.grid(row=5, column=0)
        self.y4 = Label(master, text="4")
        self.y4.grid(row=6, column=0)
        self.y5 = Label(master, text="5")
        self.y5.grid(row=7, column=0)
        self.y6 = Label(master, text="6")
        self.y6.grid(row=8, column=0)
        self.y7 = Label(master, text="7")
        self.y7.grid(row=9, column=0)
        self.y8 = Label(master, text="8")
        self.y8.grid(row=10, column=0)
        self.y9 = Label(master, text="9")
        self.y9.grid(row=11, column=0)
        self.x0 = Label(master, text="0")
        self.x0.grid(row=1, column=1)
        self.x1 = Label(master, text="1")
        self.x1.grid(row=1, column=2)
        self.x2 = Label(master, text="2")
        self.x2.grid(row=1, column=3)
        self.x3 = Label(master, text="3")
        self.x3.grid(row=1, column=4)
        self.x4 = Label(master, text="4")
        self.x4.grid(row=1, column=5)
        self.x5 = Label(master, text="5")
        self.x5.grid(row=1, column=6)
        self.x6 = Label(master, text="6")
        self.x6.grid(row=1, column=7)
        self.x7 = Label(master, text="7")
        self.x7.grid(row=1, column=8)
        self.x8 = Label(master, text="8")
        self.x8.grid(row=1, column=9)
        self.x9 = Label(master, text="9")
        self.x9.grid(row=1, column=10)

        self.label = Label(master, text=f"Shots: {shots}")
        self.label.grid(row=12, column=0, columnspan=11)

    def restart(self):
        self.master.destroy()
        root = Tk()
        app = Battleships(root)
        root.mainloop()


root = Tk()
app = Battleships(root)
root.mainloop()
