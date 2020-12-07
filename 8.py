# entry widget and grid layout concept
from tkinter import *
def getvals():
    print(uservalue.get())
    print(passvalue.get())
main=Tk()
main.geometry("500x500")
user=Label(main,text="username")
password=Label(main,text="password")
user.grid()
password.grid(row=1)
'''grid function ke andar row or column de sakte hai yaha maine bas row diya hai 
row=0 and column=0 default hota hai nahi likho fir bhi'''
# variable classes in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar
uservalue=StringVar()       # uservalue string hogi
passvalue=StringVar()
userentry=Entry(main,textvariable=uservalue)
'''uservalue ko box me lane ke liye textvariable ka use kara hai,
entry karwane ke liye textvariable ka use karte hai'''
passentry=Entry(main,textvariable=passvalue)
userentry.grid(row=0 ,column=1)
passentry.grid(row=1 ,column=1)
Button(text='submit',command=getvals).grid()
'''command=function ka naam  dene se ye hota hai ki jab button click karte hai to
control function ke pass chala jata hai or usme jo likha hai wo print ho jata hai'''
main.mainloop()