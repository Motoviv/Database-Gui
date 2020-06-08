#form design and take input
from tkinter import *
import sqlite3
t=Tk()
t.geometry("400x400")
a= StringVar()
b=StringVar()

def show():
    db= sqlite3.connect('student.db')
    cr=db.cursor()
    cr.execute("Insert into login values('"+a.get()+"','"+b.get()+"')")
    db.commit()
    db.close()
    print("Data inserted")
    a.set("")
    b.set("")

e1=Entry(font =("",11),textvariable=a)
e1.pack()

e2=Entry(font =("",11),textvariable=b)
e2.pack()

b1=Button(text ="Insert..",font=("",15),command=show)
b1.pack()


t.mainloop()