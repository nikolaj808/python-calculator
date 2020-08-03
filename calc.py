# IMPORTS AND GLOBALS

from tkinter import *
expression = "0"

# FUNCTIONS

def buttonPress(inputExpression):
	global expression
	if inputExpression == "DEL":
		if expression != "0":
			expression = expression[0:len(expression)-1]
			if expression == "":
				expression = "0"
	elif inputExpression == "CE":
		expression = "0"
	elif inputExpression == "()":
		expression = "(" + expression + ")"
	else:
		if expression == "0":
			expression = ""
		expression = expression + inputExpression
	equation.set(expression)

def equals():
	global expression
	expression = str(eval(expression))
	equation.set(expression)

# INITIALISATION

gui = Tk()

gui.geometry("450x550+300+300")
gui.title("Very Simple Calculator")
equation = StringVar()
equation.set(expression)

# INPUT FIELD AND BUTTON ROWS

label1 = Label(gui, textvariable=equation, anchor=E, bg="#1C1C1C", fg="white", font=("Elephant", 32))
label1.pack(expand=True, fill=BOTH)

btnrow1 = Frame(gui, bg="#000000")
btnrow1.pack(expand=True, fill=BOTH)

btnrow2 = Frame(gui, bg="#000000")
btnrow2.pack(expand=True, fill=BOTH)

btnrow3 = Frame(gui, bg="#000000")
btnrow3.pack(expand=True, fill=BOTH)

btnrow4 = Frame(gui, bg="#000000")
btnrow4.pack(expand=True, fill=BOTH)

# ROW 1

btn7 = Button(btnrow1, text="7", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("7"))
btn7.pack(side=LEFT, expand=True, fill=BOTH)

btn8 = Button(btnrow1, text="8", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("8"))
btn8.pack(side=LEFT, expand=True, fill=BOTH)

btn9 = Button(btnrow1, text="9", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("9"))
btn9.pack(side=LEFT, expand=True, fill=BOTH)

btndivide = Button(btnrow1, text="\u00F7", font=("Elephant", 22), width=1, bg="#2E2E2E", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("/"))
btndivide.pack(side=LEFT, expand=True, fill=BOTH)

btnDEL = Button(btnrow1, text="DEL", font=("Elephant", 22), width=1, bg="#2E2E2E", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("DEL"))
btnDEL.pack(side=LEFT, expand=True, fill=BOTH)

# ROW 2

btn4 = Button(btnrow2, text="4", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("4"))
btn4.pack(side=LEFT, expand=True, fill=BOTH)

btn5 = Button(btnrow2, text="5", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("5"))
btn5.pack(side=LEFT, expand=True, fill=BOTH)

btn6 = Button(btnrow2, text="6", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("6"))
btn6.pack(side=LEFT, expand=True, fill=BOTH)

btnx = Button(btnrow2, text="\u00D7", font=("Elephant", 22), width=1, bg="#2E2E2E", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("*"))
btnx.pack(side=LEFT, expand=True, fill=BOTH)

btnCE = Button(btnrow2, text="CE", font=("Elephant", 22), width=1, bg="#2E2E2E", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("CE"))
btnCE.pack(side=LEFT, expand=True, fill=BOTH)

# ROW 3

btn1 = Button(btnrow3, text="1", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("1"))
btn1.pack(side=LEFT, expand=True, fill=BOTH)

btn2 = Button(btnrow3, text="2", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("2"))
btn2.pack(side=LEFT, expand=True, fill=BOTH)

btn3 = Button(btnrow3, text="3", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("3"))
btn3.pack(side=LEFT, expand=True, fill=BOTH)

btnminus = Button(btnrow3, text="-", font=("Elephant", 22), width=1, bg="#2E2E2E", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("-"))
btnminus.pack(side=LEFT, expand=True, fill=BOTH)

btnmodulus = Button(btnrow3, text="%", font=("Elephant", 22), width=1, bg="#2E2E2E", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("%"))
btnmodulus.pack(side=LEFT, expand=True, fill=BOTH)

# ROW 4

btncomma = Button(btnrow4, text=",", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("."))
btncomma.pack(side=LEFT, expand=True, fill=BOTH)

btn0 = Button(btnrow4, text="0", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("0"))
btn0.pack(side=LEFT, expand=True, fill=BOTH)

btnparenteses = Button(btnrow4, text="()", font=("Elephant", 22), width=1, bg="#000000", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("()"))
btnparenteses.pack(side=LEFT, expand=True, fill=BOTH)

btnplus = Button(btnrow4, text="+", font=("Elephant", 22), width=1, bg="#2E2E2E", fg="white", relief="ridge", highlightthickness=0, bd=0, command=lambda: buttonPress("+"))
btnplus.pack(side=LEFT, expand=True, fill=BOTH)

btnequals = Button(btnrow4, text="=", font=("Elephant", 22), width=1, bg="#DF0101", fg="white", relief="ridge", highlightthickness=0, bd=0, command=equals)
btnequals.pack(side=LEFT, expand=True, fill=BOTH)

# MAINLOOP

gui.mainloop()