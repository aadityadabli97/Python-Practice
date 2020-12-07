# concept of Label and pack(attributes of Label and pack)
from tkinter import *
from tkinter.font import Font
main=Tk()
main.geometry('1200x700')
main.title("my GUI ")
# adds the text
# title=adds the text
# bg=background
# fg=foreground
# font=sets the font
# 1>font=("comicsansms",19,'bold')
# padx=x padding
# pady=y padding
# relief=border styling -SUNKEN,RAISED,GROOVE,RIDGE
myfont=Font(family="Times New Roman ",size="66")
label=Label(text='''Ready''', bg='red',fg='green', padx=10, pady=5,font=myfont, borderwidth =5, relief=RIDGE)
# IMPORTANT PACK OPTIONS
# anchor=nw,ne,sw,se
# side=TOP,BOTTOM,LEFT,RIGHT

label.pack(side=TOP ,fill=Y ,pady=50)

main.mainloop()
