from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")
content = ttk.Frame(root)


class Functions:
    def __init__():
        # num1 is the first number in the equation ex.(3+5, in this case num1 would be 3)
        global num1
        num1 = 0
        test = 0
        # num2 is the second number in the equation ex.(3+5, in this case num2 would be 5)
        global num2
        num2 = 0

    def button_click(number):
        if num1 != 0:
            input.delete(0, END)
        current = input.get()
        input.delete(0, END)
        input.insert(0, str(current) + str(number))

    def button_add(number):
        global num1
        input.delete(0, END)
        if num1 == 0:
            num1 = number
            print("num1: " + num1)
        else:
            print("num1: " + str(num1))
            print("number: " + str(number))
            num1 = int(num1) + int(number)
            print("num1: " + str(num1))
            input.insert(0, num1)



    def button_equals(number, num1):
        global num2
        num2 = number
        input.delete(0, END)
        if num1 != 0:
            print("num1: " + str(num1))
            print("num2: " + str(num2))
            print(int(num1) + int(num2))
            input.insert(0, int(num1) + int(num2))
        else:
            num1 = num2
            print(num1)
            input.insert(0, num1)

    def button_clear():
        input.delete(0, END)
        global num1
        num1 = 0
        global num2
        num2 = 0


# initialize buttons

input = ttk.Entry(content, width=40, justify="right")

button1 = Button(content, text=1, width=10, height=3, command=lambda: Functions.button_click(1))
button2 = Button(content, text=2, width=10, height=3, command=lambda: Functions.button_click(2))
button3 = Button(content, text=3, width=10, height=3, command=lambda: Functions.button_click(3))
button4 = Button(content, text=4, width=10, height=3, command=lambda: Functions.button_click(4))
button5 = Button(content, text=5, width=10, height=3, command=lambda: Functions.button_click(5))
button6 = Button(content, text=6, width=10, height=3, command=lambda: Functions.button_click(6))
button7 = Button(content, text=7, width=10, height=3, command=lambda: Functions.button_click(7))
button8 = Button(content, text=8, width=10, height=3, command=lambda: Functions.button_click(8))
button9 = Button(content, text=9, width=10, height=3, command=lambda: Functions.button_click(9))
button0 = Button(content, text=0, width=10, height=3, command=lambda: Functions.button_click(0))

add_button = Button(content, text="+", width=10, height=3, command=lambda: Functions.button_add(input.get()))
clear_button = Button(content, text="clear", width=10, height=3, command=Functions.button_clear)
equals_button = Button(content, text="=", width=10, height=3, command=lambda: Functions.button_equals(input.get(), num1))

# arrange input and buttons on grid

content.grid(column=0, row=0)

input.grid(column=0, row=0, columnspan=3)

button9.grid(column=2, row=1)
button8.grid(column=1, row=1)
button7.grid(column=0, row=1)

button6.grid(column=2, row=2)
button5.grid(column=1, row=2)
button4.grid(column=0, row=2)

button1.grid(column=0, row=3)
button2.grid(column=1, row=3)
button3.grid(column=2, row=3)

button0.grid(column=0, row=4)

clear_button.grid(column=2, row=4)
add_button.grid(column=3, row=1)
equals_button.grid(column=1, row=4)


Functions.__init__()
root.mainloop()
