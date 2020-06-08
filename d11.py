from tkinter import *
import  sqlite3
from tkinter import messagebox

t=Tk()
t.geometry("500x350")

s1=StringVar()
s2=StringVar()

u1=Label(text="Enter Name",font =("",11))
u1.place(x=100,y=100)
e1=Entry(font=("",12),textvariable=s1)
e1.place(x=200,y=100,width=120)

u2=Label(text="Enter Password",font=("",11))
u2.place(x=100,y=150)
e2=Entry(font=(",12"),show='*',textvariable=s2)
e2.place(x=200,y=150,width=120)

def show1():
    db = sqlite3.connect('student.db')
    cr = db.cursor()
    r = cr.execute("select * from login where  UNAME ='" + s1.get() + "' AND UPASS ='" + s2.get() + "'")
    for r1 in r:
        #print("welcome")
        messagebox.showinfo("Title","Welcome")
        break
    else:
        #print("invalid username and password")
        messagebox.showinfo("Title","invalid username and password")

    db.commit()
    db.close()

b1=Button(text="LOGIN",font=("",14),bg="blue",command=show1)
b1.place(x=150,y=200)
t.mainloop()