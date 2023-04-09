from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from datetime import datetime as dt
import pymongo

fg_color = '#121212'

def handleSubmit():
    myclient = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = myclient['pydb']
    mycol = mydb['students']
    data = {
        "Name": a,
        "Password": b
    }
    user= mycol.find_one({"Name": data['Name'], "Password": data['Password']})
    if user == None:
        showerror('KISIKO COLLEDGE','NAME OR PASSWORD MISSMATCH OR USER DOESNOT EXIT')
    else:
        showinfo('KISIKO COLLEDGE', data['Name'].upper()+' WELCOME BACK .....')
        clear()
        jay.destroy()
        import main_window


def clear():
    e1.delete(0,END)
    e2.delete(0,END)


def subbmit():
    global a, b
    a=e1.get()
    b=e2.get()
    if a or b != '':
        handleSubmit()
    else:
        showwarning('KISIKO COLLEGE','ALL FIELDS ARE REQUIRED')

def focus_1(e):
    e2.focus_set()
def focus_2(e):
    subbmit()

def timer():
    time=dt.now()
    x=time.strftime('%H:%M:%S  %p')
    y=time.strftime('%A  %d  %b  %Y')
    lb.config(text=x)
    lb1.config(text=y)
    canvas.after(1000,timer)

def toMain():
    exitting=askquestion('KISIKO COLLEGE','QUIT TASK')
    if exitting=='yes':
        jay.destroy()
        import main_window

jay=Tk()
jay.title('KISIKO COLLEGE')
canvas=Canvas(jay,width=500,height=250)
canvas.pack()
canvas.create_text(255,30,text='LOGGING FORM',fill='#654321',font=('algerian',24,'bold underline'))
lb=Label(canvas,fg=fg_color, font=('segoe script', 15,'bold'))
lb.place(x=50,y=60)
lb1=Label(canvas,fg=fg_color, font=('segoe script', 12))
lb1.place(x=250,y=60)
stud=1
canvas.create_text(90,130,text='FULL NAME',fill=fg_color,font=('verdana',15,'bold'))
e1=Entry(canvas,font=('arial view',15),fg=fg_color)
canvas.create_text(84,180,text='PASSWORD',fill=fg_color,font=('verdana',15,'bold'))
e2=Entry(canvas,font=('arial view',15),fg=fg_color,show='*')
back=ttk.Button(canvas,text='BACK',command=toMain)
back.place(x=20,y=210)
canvas.create_text(250,630,text=' @ 2023   Designed by Jaymoh',font=('ink free',15),fill=fg_color)
sub=ttk.Button(canvas,text='SUBMIT',command=subbmit)
sub.place(x=400,y=210)
e1.place(x=200,y=118)
e2.place(x=200,y=166)
e1.bind('<Return>',focus_1)
e2.bind('<Return>',focus_2)
timer()
mainloop()