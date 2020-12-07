# concept of listbox
from tkinter import  *
main=Tk()
main.geometry("500x500")
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0
main.title("listbox concept in tkinter")
lbx=Listbox(main)      # listbox ek dabba ban jaega jiske andar dalte raho
lbx.pack()
lbx.insert(END,"first item of a listbox")
Button(main,text="add item",command=add).pack()
main.mainloop()