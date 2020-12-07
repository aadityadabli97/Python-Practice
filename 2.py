# concept of making window in tkinter using geometry
from tkinter import *
main=Tk()
# width x height is the syntax used here 
main.geometry("500x500")
# width,height is the syntax used here
main.minsize(300,100)
main.maxsize(1200,988)

label= Label(text= 'welcome to pycharm community edition')
label.pack()
main.mainloop()