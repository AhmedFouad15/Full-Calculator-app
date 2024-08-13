from tkinter import *

def buttonvalue(value):
    global equation_value
    
    equation_value = equation_value + str(value)
    equation_label.set(equation_value)

def equal():
    global equation_value
    try:
       total = str(eval(equation_value))
       equation_label.set(total)

       equation_value = total

    except SyntaxError:
        equation_label.set("")
        equation_label.set("Syntax Error")


    except ZeroDivisionError:
        equation_label.set("")
        equation_label.set("can not divide by ZERO!!!")

def clear():
    global equation_value
    equation_value = ""
    equation_label.set("")

window = Tk()

window.geometry("500x370")
window.title("Calculator")

window.config(bg="Grey")

equation_value = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("Arrial", 20),bg="White", width=22, height=2)
label.pack()

frame = Frame(window, bg="Grey")
frame.pack()

button1 = Button(frame, text=1, height=2, width= 9,  bg="Grey",activebackground="Grey", font=14, command= lambda: buttonvalue(1))
button1.grid(row=1, column=0)

button2 = Button(frame, text=2, height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue(2))
button2.grid(row=1, column=1)

button3 = Button(frame, text=3, height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue(3))
button3.grid(row=1, column=2)

button4 = Button(frame, text=4, height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue(4))
button4.grid(row=2, column=0)

button5 = Button(frame, text=5, height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue(5))
button5.grid(row=2, column=1)

button6 = Button(frame, text=6, height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue(6))
button6.grid(row=2, column=2)

button7 = Button(frame, text=7, height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue(7))
button7.grid(row=3, column=0)

button8 = Button(frame, text=8, height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue(8))
button8.grid(row=3, column=1)

button9 = Button(frame, text=9, height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue(9))
button9.grid(row=3, column=2)

button0 = Button(frame, text=0, height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue(0))
button0.grid(row=4, column=1)

Divide = Button(frame, text="÷", height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue("/"))
Divide.grid(row=1 ,column=3)

Multiple = Button(frame, text="x", height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue("*"))
Multiple.grid(row=2, column=3)

plus = Button(frame, text="+", height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue("+"))
plus.grid(row=3, column=3)

Minus = Button(frame, text="-", height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command= lambda: buttonvalue("-"))
Minus.grid(row=4, column=3)

decimal = Button(frame, text=".", height=2, width= 9, font=1, bg="Grey",activebackground="Grey", command= lambda: buttonvalue("."))
decimal.grid(row=4, column=2)

delete = Button(frame, text="Clear", height=2, width= 9, font=14, bg="Grey",activebackground="Grey", command=clear)
delete.grid(row=4, column=0)

Equal = Button(window, text="=", height=1, width= 40, font=14, bg="Grey",activebackground="Grey", command=equal)
Equal.pack()

window.mainloop()