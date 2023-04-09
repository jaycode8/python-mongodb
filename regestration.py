from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.messagebox import *
from functools import partial
from datetime import datetime as dt
import pymongo

fg_color = '#121212'

def handleSubmit():
    myclient = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = myclient['pydb']
    mycol = mydb['students']
    record = {
        "Name": a+' '+b,
        "Address":c,
        "sex":d,
        "city":e,
        "course": f,
        "Mobile":g,
        "DOB": h+'-'+i+'-'+j,
        "Password": k
    }
    mycol.insert_one(record)
    showinfo('KISIKO COLLEGE', record['Name'].upper()+' SUCCESSFULLY REGESTERED')
    clear()
    jay.destroy()
    import main_window


def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e7.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)


def subbmit():
    global e1
    global e2
    global e3
    global a, b, c, d, e, f , g, h, i, j, k
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    f=e6.get()
    g=e7.get()
    h=e8.get()
    i=e9.get()
    j=e10.get()
    k=e11.get()
    l=e12.get()
    if a or b or c or g or k or l!= '':
        if ep.get()==cp.get():
            handleSubmit()
        else:
            showwarning('KISIKO COLLEGE','PASSWORD MISSMATCH')
    else:
        showwarning('KISIKO COLLEGE','ALL FIELDS ARE REQUIRED')

def focus_1(e):
    e2.focus_set()
def focus_2(e):
    e3.focus_set()
def focus_3(e):
    e4.focus_set()
def focus_4(e):
    e5.focus_set()
def focus_5(e):
    e6.focus_set()
def focus_6(e):
    e7.focus_set()
def focus_7(e):
    e8.focus_set()
def focus_8(e):
    e9.focus_set()
def focus_9(e):
    e10.focus_set()
def focus_10(e):
    e11.focus_set()
def focus_11(e):
    e12.focus_set()
def focus_12(e):
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
canvas=Canvas(jay,width=500,height=650)
canvas.pack()
canvas.create_text(255,30,text='STUDENT REGESTRATION FORM',fill='#654321',font=('algerian',24,'bold underline'))
lb=Label(canvas,fg=fg_color, font=('segoe script', 15,'bold'))
lb.place(x=50,y=60)
lb1=Label(canvas,fg=fg_color, font=('segoe script', 12))
lb1.place(x=250,y=60)
stud=1
canvas.create_text(90,130,text='FIRST NAME',fill=fg_color,font=('verdana',15,'bold'))
e1=Entry(canvas,font=('arial view',15),fg=fg_color)
canvas.create_text(84,180,text='LAST NAME',fill=fg_color,font=('verdana',15,'bold'))
e2=Entry(canvas,font=('arial view',15),fg=fg_color)
canvas.create_text(72,230,text='ADDRESS',fill=fg_color,font=('verdana',15,'bold'))
e3=Entry(canvas,font=('arial view',15),fg=fg_color)
canvas.create_text(49,280,text='SEX',fill=fg_color,font=('verdana',15,'bold'))
e4=Combobox(canvas,font=('arial view',10,'bold'),width=27)
e4['value']=('MALE','FEMALE')
e4.current(0)
canvas.create_text(55,330,text='CITY',fill=fg_color,font=('verdana',15,'bold'))
e5=Combobox(canvas,font=('arial view',10,'bold'),width=27)
e5['values']=('Nairobi','Mombas','Kisumu','Nakuru','wote')
e5.current(0)
canvas.create_text(67,380,text='COURSE',fill=fg_color,font=('verdana',15,'bold'))
e6=Combobox(canvas,font=('arial view',10,'bold'),width=27)
e6['value']=('Computer Science','Education','Business Management')
e6.current(0)
canvas.create_text(66,430,text='MOBILE',fill=fg_color,font=('verdana',15,'bold'))
e7=Entry(canvas,font=('arial view',15),fg=fg_color)
canvas.create_text(50,480,text='DOB',fill=fg_color,font=('verdana',15,'bold'))
e8=Combobox(canvas,font=('arial view',10,'bold'),width=4)
e8['value']=('01','02','03','04','05','06','07','08','09',10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
e8.current(0)
e9=Combobox(canvas,font=('arial view',10,'bold'),width=5)
e9['value']=('JAN','FEB','MAR','APRI','MAY','JUNE','JULY','AUG','SEP','OCT','NOV','DEC')
e9.current(0)
e10=Combobox(canvas,font=('arial view',10,'bold'),width=4)
e10['value']=(1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008)
e10.current(0)
canvas.create_text(80,530,text='PASSWORD',fill=fg_color,font=('verdana',15,'bold'))
ep=StringVar()
e11=Entry(canvas,font=('arial view',15),fg=fg_color,textvariable=ep,show='*')
canvas.create_text(73,580,text='CONFIRM',fill=fg_color,font=('verdana',15,'bold'))
cp=StringVar()
e12=Entry(canvas,font=('arial view',15),fg=fg_color,textvariable=cp,show='*')
validatepassword=partial(subbmit,ep,cp)
back=ttk.Button(canvas,text='BACK',command=toMain)
back.place(x=20,y=620)
canvas.create_text(250,630,text=' @ 2021   Designed by Jaymoh',font=('ink free',15),fill=fg_color)
sub=ttk.Button(canvas,text='SUBMIT',command=subbmit)
sub.place(x=400,y=620)
e1.place(x=200,y=118)
e2.place(x=200,y=166)
e3.place(x=200,y=214)
e4.place(x=200,y=265)
e5.place(x=200,y=316)
e6.place(x=200,y=366)
e7.place(x=200,y=415)
e8.place(x=200,y=468)
e9.place(x=280,y=468)
e10.place(x=360,y=468)
e11.place(x=200,y=515)
e12.place(x=200,y=565)
e1.bind('<Return>',focus_1)
e2.bind('<Return>',focus_2)
e3.bind('<Return>',focus_3)
e4.bind('<Return>',focus_4)
e5.bind('<Return>',focus_5)
e6.bind('<Return>',focus_6)
e7.bind('<Return>',focus_7)
e8.bind('<Return>',focus_8)
e9.bind('<Return>',focus_9)
e10.bind('<Return>',focus_10)
e11.bind('<Return>',focus_11)
e12.bind('<Return>',focus_12)
timer()
mainloop()