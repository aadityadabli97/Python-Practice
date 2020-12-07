# concept of frame in tkinter
from tkinter import*
aaditya=Tk()
aaditya.geometry("344x500")
f1=Frame(aaditya,bg='yellow',bd=15,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
l=Label(f1,text="project tkinter")  #label ko frame ke andar pack karte hai , tabhi label frame ke andar aayega
f2=Frame(aaditya,bg='grey',relief=SUNKEN,bd=15)
l2=Label(f2,text=' USAGE OF FRAME ',bg="red",fg="green",font="bold")
f2.pack(side=TOP,fill="x")
l.pack(padx=10)
l2.pack(pady=100)
aaditya.mainloop()