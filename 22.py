# concept of how to change icon in tkinter window
from  tkinter import *
main=Tk()
main.geometry("555x555")
main.wm_iconbitmap("rose.ico")       # function to change icon
# function to change window background color
main.configure(background="red")
# screen width and height
width=main.winfo_screenmmwidth()
height=main.winfo_screenheight()
print(f"{width}x{height}")
# closing window using button
Button(text="close",command=main.destroy).pack()
main.mainloop()
