# concept of status bar in tkinter
from tkinter import*
def upload():
    statusvar.set("busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready now")
main=Tk()

main.title("status bar ")
statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(main,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(main,text="upload",command=upload).pack()
main.geometry("500x500")
main.mainloop()