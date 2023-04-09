from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

def toReg():
    jaymoh.destroy()
    import regestration

def toLog():
    jaymoh.destroy()
    import log
    
def exitting():
    exitt=askquestion('KISIKO COLLEGE','DO YO WANT TO QUIT APPLICATION !!')
    if exitt=='yes':
        exit()
        
jaymoh=Tk()
jaymoh.title('KISIKO COLLEGE')
jaymoh.geometry('550x550')
can=Canvas(jaymoh,width=550,height=550)
can.pack()
can.create_text(270,50,text='KISIKO COLLEGE',font=('algerian',40,'bold underline'),fill='red')
can.create_text(250,150,text='Education is the key',font=('ink free',23,'bold'),fill='#980989')
bt=Button(can,text='REG',font=('ink free',20,'bold'),fg='green',command=toReg)
bt.place(x=100,y=400)
bt1=Button(can,text='LOG',font=('ink free',20,'bold'),fg='green', command=toLog)
bt1.place(x=350,y=400)
back=ttk.Button(can,text='EXIT',command=exitting)
back.place(x=225,y=515)
mainloop()