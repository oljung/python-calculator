from tkinter import *
from math import *
root = Tk()
root.geometry("210x270")
root.title("Kalkylator")

def calculatorTitle():
	labelTitle=Label(root, text = "Kalkylator", bg = "black", fg = "white")
	labelTitle.config(font=("Verbana", 12, "bold"))
	labelTitle.place(x=100, y=0)

e = Entry(root, width=20, font="Arial 12", justify="right", bg="black", fg="white")
e.place(x=15, y=30)

def addEntry(ch):
	e.insert(20, ch)

def clear():
	e.delete(0, END)

def calculateEntry(expression):
	e.delete(0, END)
	e.insert(20, expression)

def exp():
	number = float(e.get())
	e.delete(0, END)
	exponent = 0
	if number > 1:
		while number > 1:
			number = number/10
			exponent += 1
		e.insert(20, f'{number}x10^{exponent}')
	if number < 1:
		while number < 1:
			number = number*10
			exponent += 1
		e.insert(20, f'{number}x10^-{exponent:.0f}')


def calcylatorBoard():
	b1=Button(root, text='1', width=5, command=lambda:addEntry(1))
	b1.place(x=10, y=150)
	b2=Button(root, text='2', width=5, command=lambda:addEntry(2))
	b2.place(x=60, y=150)
	b3=Button(root, text='3', width=5, command=lambda:addEntry(3))
	b3.place(x=110, y=150)
	b4=Button(root, text='4', width=5, command=lambda:addEntry(4))
	b4.place(x=10, y=120)
	b5=Button(root, text='5', width=5, command=lambda:addEntry(5))
	b5.place(x=60, y=120)
	b6=Button(root, text='6', width=5, command=lambda:addEntry(6))
	b6.place(x=110, y=120)
	b7=Button(root, text='7', width=5, command=lambda:addEntry(7))
	b7.place(x=10, y=90)
	b8=Button(root, text='8', width=5, command=lambda:addEntry(8))
	b8.place(x=60, y=90)
	b9=Button(root, text='9', width=5, command=lambda:addEntry(9))
	b9.place(x=110, y=90)
	b10=Button(root, text='0', width=5, command=lambda:addEntry(0))
	b10.place(x=10, y=180)
	b11=Button(root, text='(', width=5, bg='gray60', command=lambda:addEntry('('))
	b11.place(x=10, y=60)
	b12=Button(root, text=')', width=5, bg='gray60', command=lambda:addEntry(')'))
	b12.place(x=60, y=60)
	b13=Button(root, text='\u03c0', command=lambda:addEntry('pi'))
	b13.place(x=110, y=60)
	b14=Button(root, text='e', command=lambda:addEntry('e'))
	b14.place(x=135, y=60)
	b15=Button(root, text='CE', width=5, fg='red', command=clear)
	b15.place(x=160, y=60)
	b16=Button(root, text='.', width=5, command=lambda:addEntry('.'))
	b16.place(x=60, y=180)
	bEqual=Button(root, text='=', width=5, bg='dodger blue', command=lambda:calculateEntry(eval(e.get())))
	bEqual.place(x=110, y=180)
	b17=Button(root, text='+', width=5, bg='chocolate1', command=lambda:addEntry('+'))
	b17.place(x=160, y=90)
	b18=Button(root, text='-', width=5, bg='chocolate1', command=lambda:addEntry('-'))
	b18.place(x=160, y=120)
	b19=Button(root, text='\u00F7', width=5, bg='chocolate1', command=lambda:addEntry('/'))
	b19.place(x=160, y=150)
	b18=Button(root, text='x', width=5, bg='chocolate1', command=lambda:addEntry('*'))
	b18.place(x=160, y=180)
	b18=Button(root, text='\u221a', width=5, fg='blue', command=lambda:addEntry('sqrt('))
	b18.place(x=10, y=210)
	b19=Button(root, text='x^2', width=5, fg='blue', command=lambda:addEntry('**2'))
	b19.place(x=60, y=210)
	b20=Button(root, text='x^y', width=5, fg='blue', command=lambda:addEntry('**'))
	b20.place(x=110, y=210)
	b21=Button(root, text='EXP', width=5, fg='blue', command=exp)
	b21.place(x=160, y=210)
	b22=Button(root, text='sin', width=5, fg='green', command=lambda:addEntry('sin('))
	b22.place(x=10, y=240)
	b23=Button(root, text='cos', width=5, fg='green', command=lambda:addEntry('cos('))
	b23.place(x=60, y=240)
	b24=Button(root, text='tan', width=5, fg='green', command=lambda:addEntry('tan('))
	b24.place(x=110, y=240)
	b25=Button(root, text='ln', width=5, command=lambda:addEntry('log('))
	b25.place(x=160, y=240)

calculatorTitle()
calcylatorBoard()
root.mainloop()

