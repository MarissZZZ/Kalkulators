from distutils import command
from hashlib import new
from math import*
import distutils
import numbers
import string
from tkinter import*
from turtle import color # importē bibiliotēku
from unittest.util import strclass
import tkinter as tk

mansLogs=Tk()
mansLogs.title('Kalkulators')



#================================================================================================================
def btnClick(number):
    current=e.get() # nolasa esošo skaitli
    e.delete(0,END) # nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) # ievieto displejā
    return 0

#================================================================================================================
def btnCommand(command):
    global number #jāiegaumē skaitlis un darbība
    global mathOp #matemātiskais operators
    global num1
    global num3
    mathOp=command #+-*/
    num1=(float(e.get()))
    e.delete(0,END)
    return 0

#================================================================================================================
def vienads():
    global num2
    num2=(float(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

#================================================================================================================
def sq_rt():
    global operator
    global num1
    global mathOp
    num1=(float(e.get()))
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)
    return 0

#================================================================================================================
def kvad():
    global operator
    global num1
    global mathOp
    num1=(float(e.get())**2)
    e.delete(0,END)
    e.insert(0,num1)
    return 0
#================================================================================================================
def min():
    global operator
    global mathOp #matemātiskais operators
    global num1
    num1=-(float(e.get()))
    e.delete(0,END)
    e.insert(0,str(num1))
    return 0

#================================================================================================================
def logoritms():
    global operator
    global mathOp #matemātiskais operators
    global num1
    num1=(float(e.get()))
    num1=log(num1,10)
    e.delete(0,END)
    e.insert(0,str(num1))
    return 0

#================================================================================================================
def notirit():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0

#================================================================================================================
def punkts():
    if e.get()==".":
        pass
    else:
        e.insert(END,'.')

#================================================================================================================
e=Entry(mansLogs,width=15,bd=20,font=("Arial Black",20))
#================================================================================================================
btn0=Button(mansLogs,text='0',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='white', command=lambda:btnClick(0))
btn1=Button(mansLogs,text='1',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='white', command=lambda:btnClick(1))
btn2=Button(mansLogs,text='2',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='white', command=lambda:btnClick(2))
btn3=Button(mansLogs,text='3',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='white', command=lambda:btnClick(3))
btn4=Button(mansLogs,text='4',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='white', command=lambda:btnClick(4))
btn5=Button(mansLogs,text='5',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='white', command=lambda:btnClick(5))
btn6=Button(mansLogs,text='6',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='white', command=lambda:btnClick(6))
btn7=Button(mansLogs,text='7',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='white', command=lambda:btnClick(7))
btn8=Button(mansLogs,text='8',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='white', command=lambda:btnClick(8))
btn9=Button(mansLogs,text='9',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='white', command=lambda:btnClick(9))
btnAdd=Button(mansLogs,text='+',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='cyan', command=lambda:btnCommand("+"))
btnSub=Button(mansLogs,text='-',padx='43',pady='20', bd=10, font=('Arial Black',20), bg='cyan', command=lambda:btnCommand("-"))
btnReiz=Button(mansLogs,text='*',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='cyan', command=lambda:btnCommand("*"))
btnDal=Button(mansLogs,text='/',padx='43',pady='20', bd=10, font=('Arial Black',20), bg='cyan', command=lambda:btnCommand("/"))
btnC=Button(mansLogs,text='C',padx='39',pady='20', bd=10, font=('Arial Black',20), fg='red', bg='cyan', command=notirit)
btnVien=Button(mansLogs,text='=',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='cyan', command=vienads)
btnKom=Button(mansLogs,text='log',padx='25.5',pady='20', bd=10, font=('Arial Black',20), bg='cyan', command=logoritms)
btnPlusMin=Button(mansLogs,text='+/-',padx='31',pady='20', bd=10, font=('Arial Black',20), bg='cyan', command=min)
btnIek=Button(mansLogs,text='x²',padx='34.5',pady='20', bd=10, font=('Arial Black',20), bg='cyan', command=kvad)
btnProc=Button(mansLogs,text='√',padx='41.4',pady='20', bd=10, font=('Arial Black',20), bg='cyan', command=sq_rt)
btnPunkts=Button(mansLogs,text='.',padx='40',pady='20', bd=10, font=('Arial Black',20), bg='cyan', command=punkts)

#================================================================================================================
e.grid(row=0,column=0,columnspan=4) # ievieto režģī
#================================================================================================================
btnPlusMin.grid(row=5,column=0)
btnIek.grid(row=1,column=1)
btnProc.grid(row=1,column=2)
btnVien.grid(row=5,column=3)
btnKom.grid(row=5,column=2)
btnC.grid(row=1,column=0)
btnAdd.grid(row=4,column=3)
btnSub.grid(row=3,column=3)
btnReiz.grid(row=2,column=3)
btnDal.grid(row=1,column=3)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)

btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)

btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)

btn0.grid(row=5,column=1)

#================================================================================================================


mansLogs.mainloop()