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
u1= Label(text="Enter Name")
u1.place(x=100,y=50)
e1=Entry(font =("",11),textvariable=a)
e1.place(x=200,y=50)

u2= Label(text="Enter Password")
u2.place(x=100,y=100)
e2=Entry(font =("",11),textvariable=b,show ='*')
e2.place(x=200,y=100)

b1=Button(text ="Insert..",font=("",15),bg="pink",command=show)
b1.place(x=150,y=150)


t.mainloop()