#delete page
from tkinter import *
import  sqlite3
from tkinter import messagebox

t=Tk()
t.geometry("500x350")

s1=StringVar()

u1=Label(text="Enter Name",font =("",11))
u1.place(x=100,y=100)
e1=Entry(font=("",12),textvariable=s1)
e1.place(x=200,y=100,width=120)

def show1():
    db = sqlite3.connect('student.db')
    cr = db.cursor()
    r = cr.execute("delete from login where  UNAME ='"+s1.get()+"'")
    messagebox.showinfo("Title","Data deleted")

    db.commit()
    db.close()

b1=Button(text="DELETE",font=("",14),bg="yellow",command=show1)
b1.place(x=150,y=160)
t.mainloop()