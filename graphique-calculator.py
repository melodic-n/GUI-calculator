from tkinter import *
import math

#the app window

window = Tk()
window.iconbitmap("C:/Users/MH/Downloads/calculator.ico")

#local variable

expression = ""

#function press

def press(a):
    global expression
    expression += str(a)
    equation.set(expression)

#fonction clear
def clear():
    global expression
    expression=""
    equation.set("")

#fonction equal
    
def equal():
        global expression
        equal =str(eval(expression))
        equation.set(equal)
        expression=""
#function reverse
def reverse():
    global expression
    expression=str(1/int(expression))
    equation.set(float(expression))

        

#funtion sqrt
def sqrt():
    global expression
    equation.set(str(math.sqrt(int(expression))))
    




#---------------------------------------------

#windpw application

window.geometry('320x195')
window.title("calculator app")

#equation

equation = StringVar()

#entry screen

screen=Entry(window,width=20,textvariable = equation)
screen.grid(column=1,row=1)
screen.grid(columnspan=6, ipadx=70,padx=5,pady=5)
#plus button

button_plus=Button(window,text="+",bg="lightgray",fg="black",width=5,height=3,command = lambda:press("+"))
button_plus.grid(column=4,row=5)

#minus button

button_moin=Button(window,text="-",bg="lightgray",fg="black",width=5,height=3,command = lambda:press("-"))
button_moin.grid(column=4,row=6)

#multplication button

button_multi=Button(window,text="x",bg="lightgray",fg="black",width=5,height=3,command = lambda:press("*"))
button_multi.grid(column=6,row=6)

#division button

button_div=Button(window,text="/",bg="lightgray",fg="black",width=5,height=3,command = lambda:press("/"))
button_div.grid(column=6,row=7)

#button 1

button_1=Button(window,text="7",bg="lightgray",fg="black",width=5,height=3,command=lambda : press(7))
button_1.grid(column=1,row=5)

#button 2

button_2=Button(window,text="8",bg="lightgray",fg="black",width=5,height=3,command=lambda :press(8))
button_2.grid(column=2,row=5)

#button 3

button_3=Button(window,text="9",bg="lightgray",fg="black",width=5,height=3,command=lambda :press(9))
button_3.grid(column=3,row=5)

#button 4
button_4=Button(window,text="4",bg="lightgray",fg="black",width=5,height=3,command=lambda :press(4))
button_4.grid(column=1,row=6)

#button 5

button_5=Button(window,text="5",bg="lightgray",fg="black",width=5,height=3,command=lambda :press(5))
button_5.grid(column=2,row=6)

#button 6
button_6=Button(window,text="6",bg="lightgray",fg="black",width=5,height=3,command=lambda :press(6))
button_6.grid(column=3,row=6)

#button 7

button_7=Button(window,text="1",bg="lightgray",fg="black",width=5,height=3,command=lambda :press(1))
button_7.grid(column=1,row=7)

#button 8

button_8=Button(window,text="2",bg="lightgray",fg="black",width=5,height=3,command=lambda :press(2))
button_8.grid(column=2,row=7)

#button 9

button_9=Button(window,text="3",bg="lightgray",fg="black",width=5,height=3,command=lambda :press(3))
button_9.grid(column=3,row=7)

#button power x^2

button_carre=Button(window,text="x^2",bg="lightgray",fg="black",width=5,height=3,command=lambda:press("**2"))
button_carre.grid(column=5,row=5)

#button square root

button_sqrt=Button(window,text="sqrt",bg="lightgray",fg="black",width=5,height=3,command=lambda:sqrt())
button_sqrt.grid(column=5,row=6)

#button modulo

button_modulo=Button(window,text="%",bg="lightgray",fg="black",width=5,height=3,command=lambda:press("%"))
button_modulo.grid(column=6,row=5)

#button equal

button_equal=Button(window,text="=",bg="lightgray",fg="black",width=5,height=3,command=lambda:equal())
button_equal.grid(column=4,row=7)

#button clear

button_power=Button(window,text="clear",bg="lightgray",fg="black",width=5,height=3,command = lambda:clear())
button_power.grid(column=5,row=7)

#button left parenthesis

button_lfpr=Button(window,text="(",bg="lightgray",fg="black",width=5,height=3,command=lambda:press("("))
button_lfpr.grid(column=7,row=5)

#button right parenthesis

button_rgpr=Button(window,text=")",bg="lightgray",fg="black",width=5,height=3,command=lambda:press(")"))
button_rgpr.grid(column=7,row=6)

#reverse

button_reverse=Button(window,text="1/x",bg="lightgray",fg="black",width=5,height=3,command=lambda:reverse())
button_reverse.grid(column=7,row=7)

#keep the window open
window.mainloop()


