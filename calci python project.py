from tkinter import *

window=Tk()
window.title("CALCULATOR-GUI")
window.geometry("380x350")

def btnclick(num):
    global val
    val=val+str(num)
    data.set(val)


def btnClear():
    global val
    val=""
    data.set(" ")

def btnEqual():
    global val
    res=str(eval(val))
    data.set(res)


    
val=""
data=StringVar()



display=Entry(window,bd=20,textvariable=data,justify="right",
              bg="powderblue",font=("Ariel",15,"bold"))
display.grid(row=0,column=1)
btn7=Button(window,text="7",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnclick(7))
btn7.place(x=1,y=70)
btn8=Button(window,text="8",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnclick(8))
btn8.place(x=75,y=70)
btn9=Button(window,text="9",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnclick(9))
btn9.place(x=150,y=70)
btn_add=Button(window,text="+",font=("Ariel",12,"bold"),bd=12,height=1,
            width=6,command=lambda:btnclick('+'))
btn_add.place(x=225,y=70)
btn4=Button(window,text="4",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnclick(4))
btn4.place(x=1,y=130)

btn5=Button(window,text="5",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnclick(5))
btn5.place(x=75,y=130)
btn6=Button(window,text="6",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnclick(6))
btn6.place(x=150,y=130)
btn_sub=Button(window,text="-",font=("Ariel",12,"bold"),bd=12,height=1,
            width=6,command=lambda:btnclick('-'))
btn_sub.place(x=225,y=130)
btn1=Button(window,text="1",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnclick(1))
btn1.place(x=1,y=190)
btn2=Button(window,text="2",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnclick(2))
btn2.place(x=75,y=190)
btn3=Button(window,text="3",font=("Ariel",12,"bold"),fg="black",bd=12,height=1,
            width=4,command=lambda:btnclick(3))
btn3.place(x=150,y=190)
btn_mul=Button(window,text="*",font=("Ariel",12,"bold"),fg="black",bd=12,height=1,
            width=6,command=lambda:btnclick('*'))
btn_mul.place(x=225,y=190)

btnc=Button(window,text="C",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnClear())
btnc.place(x=1,y=250)
btn0=Button(window,text="0",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnclick(0))
btn0.place(x=75,y=250)

btn_div=Button(window,text="/",font=("Ariel",12,"bold"),bd=12,height=1,
            width=4,command=lambda:btnclick('/'))
btn_div.place(x=150,y=250)

btn_equal=Button(window,text="=",font=("Ariel",16,"bold"),bd=12,height=2,
            width=4,command=lambda:btnEqual())
btn_equal.place(x=225,y=250)























