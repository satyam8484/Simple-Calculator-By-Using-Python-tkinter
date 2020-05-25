from tkinter import *
from tkinter import messagebox


def Add():
    e3.delete(0, END)
    fn = e1.get()
    sn = e2.get()
    tn = None
    try:
        tn = float(fn) + float(sn)
    except:
        messagebox.showerror('Error', 'Invalid Input')
    print(tn)
    e3.insert(0, tn)
    l3.config(text='Addition')


def Sub():
    e3.delete(0, END)
    fn = e1.get()
    sn = e2.get()
    try:
        tn = float(fn) - float(sn)
    except:
        messagebox.showerror('Error', 'Invalid Input')
    e3.insert(0, tn)
    l3.config(text='Subtraction')


def Mul():
    e3.delete(0, END)
    fn = e1.get()
    sn = e2.get()
    try:
        tn = float(fn) * float(sn)
    except:
        messagebox.showerror('Error', 'Invalid Input')
    e3.insert(0, tn)
    l3.config(text='Multiplication')


def Div():
    e3.delete(0, END)
    fn = e1.get()
    sn = e2.get()
    try:
        tn = float(fn) / float(sn)
        tn = round(tn, 2)
    except:
        messagebox.showerror('Error', 'Invalid Input')
    e3.insert(0, tn)
    l3.config(text='Division')


window = Tk()
window.title('Simple Calculator')
window.geometry('400x400+300+200')
window.config(bg='#FFF222')
window.resizable(0, 0)

l1 = Label(text='First No', bg='#FFF222', font=('Verdana', 16, 'bold'))
l1.grid(sticky=W, padx=10, pady=20)

e1 = Entry(bg='white', font=('Verdana', 10, 'bold'))
e1.grid(row=0, column=1, ipadx=3, ipady=3)

l2 = Label(text='Second No ', bg='#FFF222', font=('Verdana', 16, 'bold'))
l2.grid(row=1, column=0, sticky=W, padx=10)

e2 = Entry(bg='white', font=('Verdana', 10, 'bold'))
e2.grid(row=1, column=1, ipadx=3, ipady=3)

# Add Buttons

Add_bt = Button(text='Add', bg='#45CE30', fg='black', font=('comic sans ms', 10, 'bold'), width=8, command=Add)
Add_bt.grid(row=2, column=0, pady=25)

Sub_bt = Button(text='Sub', bg='#45CE30', fg='black', font=('comic sans ms', 10, 'bold'), width=8, command=Sub)
Sub_bt.grid(row=2, column=1)

mul_bt = Button(text='Mul', bg='#45CE30', fg='black', font=('comic sans ms', 10, 'bold'), width=8, command=Mul)
mul_bt.grid(row=3, column=0)

Div_bt = Button(text='Div', bg='#45CE30', fg='black', font=('comic sans ms', 10, 'bold'), width=8, command=Div)
Div_bt.grid(row=3, column=1)

l3 = Label(text='Result', bg='#FFF222', fg='black', font=('Verdana', 16, 'bold'))
l3.grid(row=4, column=0, sticky=W, padx=10, pady=25)

e3 = Entry(bg='white', font=('Verdana', 10, 'bold'))
e3.grid(row=4, column=1, ipadx=3, ipady=3)

window.mainloop()
