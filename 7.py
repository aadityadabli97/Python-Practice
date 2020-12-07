# concept of buttons(packing buttons in tkinter)
from tkinter import *
main=Tk()
main.geometry('400x500')
def lelo():
    print("lega kya ")
def dedo():
    print('deo na')
frame= Frame(main ,bd=15, bg='grey',relief=SUNKEN)
frame.pack(side=LEFT,anchor='ne')
b1=Button(frame,fg='red',bg='white',text="lo",command=lelo)

'''button ko frame ke andar pack karte hai tabhi 
frame ke andar button aayegi'''

b1.pack(side=LEFT,padx=10)
b2=Button(frame,fg='red',bg='white',text="do",command=dedo)
b2.pack(side=LEFT,padx=10)
b3=Button(frame,fg='red',bg='white',text="click me")
b3.pack(side=LEFT,padx=10)
b4=Button(frame,fg='red',bg='white',text="click me")
b4.pack(side=LEFT,padx=10)
main.mainloop()