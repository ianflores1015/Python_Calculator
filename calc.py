from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")

content = ttk.Frame(root)


def button_add():
    return


# define input/output box

input = ttk.Entry(content, width=50)

# Define buttons

button_1 = Button(content, text="1", padx=40, pady=20, command=button_add)
button_2 = Button(content, text="2", padx=40, pady=20, command=button_add)
button_3 = Button(content, text="3", padx=40, pady=20, command=button_add)
button_4 = Button(content, text="4", padx=40, pady=20, command=button_add)
button_5 = Button(content, text="5", padx=40, pady=20, command=button_add)
button_6 = Button(content, text="6", padx=40, pady=20, command=button_add)
button_7 = Button(content, text="7", padx=40, pady=20, command=button_add)
button_8 = Button(content, text="8", padx=40, pady=20, command=button_add)
button_9 = Button(content, text="9", padx=40, pady=20, command=button_add)
button_0 = Button(content, text="0", padx=40, pady=20, command=button_add)

#put input/output box on screen

input.grid(row=0, column=0, columnspan=3)

# Put buttons on screen

button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)

button_0.grid(row=4, column=1)

root.mainloop()
