# concept of radiobutton
from tkinter import *
import tkinter.messagebox as tmsg
main=Tk()
def order():
    tmsg.showinfo("order received",f"we have received your order for {var.get()} thanks for ordering")
main.geometry("500x500")
main.title("concept of radiobutton")
#var=IntVar()
var=StringVar()
var.set("no")
Label(main,text="what would you like to have eat?",justify=LEFT,padx=14).pack()
radio=Radiobutton(main,text="dosa",padx=14,variable=var,value='dosa').pack()
radio2=Radiobutton(main,text="idli",padx=14,variable=var,value='idli').pack()
radio3=Radiobutton(main,text="chaumin",padx=14,variable=var,value='chaumin').pack()
radio4=Radiobutton(main,text="thali",padx=14,variable=var,value='thali').pack()
Button(main,text="order now",command=order).pack()
main.mainloop()