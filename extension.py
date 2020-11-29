from tkinter import *

class Battleships:

    def __init__(self, master):
        self.master = master
        master.title("Battleships")

        '''self.label = Label(master, text="Battleships")
        self.label.grid(row=0, column=0, columnspan=11, sticky=W+E)
        self.y0 = Label(master, text="0")
        self.y0.grid(row=10, column=0)
        self.y1 = Label(master, text="1")
        self.y1.grid(row=9, column=0)
        self.y2 = Label(master, text="2")
        self.y2.grid(row=8, column=0)
        self.y3 = Label(master, text="3")
        self.y3.grid(row=7, column=0)
        self.y4 = Label(master, text="4")
        self.y4.grid(row=6, column=0)
        self.y5 = Label(master, text="5")
        self.y5.grid(row=5, column=0)
        self.y6 = Label(master, text="6")
        self.y6.grid(row=4, column=0)
        self.y7 = Label(master, text="7")
        self.y7.grid(row=3, column=0)
        self.y8 = Label(master, text="8")
        self.y8.grid(row=2, column=0)
        self.y9 = Label(master, text="9")
        self.y9.grid(row=1, column=0)
        self.x0 = Label(master, text="0")
        self.x0.grid(row=11, column=1)
        self.x1 = Label(master, text="1")
        self.x1.grid(row=11, column=2)
        self.x2 = Label(master, text="2")
        self.x2.grid(row=11, column=3)
        self.x3 = Label(master, text="3")
        self.x3.grid(row=11, column=4)
        self.x4 = Label(master, text="4")
        self.x4.grid(row=11, column=5)
        self.x5 = Label(master, text="5")
        self.x5.grid(row=11, column=6)
        self.x6 = Label(master, text="6")
        self.x6.grid(row=11, column=7)
        self.x7 = Label(master, text="7")
        self.x7.grid(row=11, column=8)
        self.x8 = Label(master, text="8")
        self.x8.grid(row=11, column=9)
        self.x9 = Label(master, text="9")
        self.x9.grid(row=11, column=10)

        self.x0y0 = Button(master, text="", width=2)
        self.x0y0.grid(row=10, column=1)
        self.x0y1 = Button(master, text="", width=2)'''





'''class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        #layout

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text:
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else:
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)'''

        
    

root = Tk()
app = Battleships(root)
root.mainloop()
