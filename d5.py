#form design and take input
from tkinter import *
t=Tk()
t.geometry("400x400")
a= StringVar()
b=StringVar()

def show():
    print(a.get(),b.get())


e1=Entry(font =("",11),textvariable=a)
e1.pack()

e2=Entry(font =("",11),textvariable=b)
e2.pack()

b1=Button(text ="Insert..",font=("",15),command=show)
b1.pack()


t.mainloop()