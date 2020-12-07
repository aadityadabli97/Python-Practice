from tkinter import *
main=Tk()
def harry(event):
    print(f"event handled at {event.x}")
main.geometry("500x500")
main.title("handling events in tkinter")
widget=Button(main,text="click me please")
widget.pack()
widget.bind("<Alt-1>",harry)
main.mainloop()