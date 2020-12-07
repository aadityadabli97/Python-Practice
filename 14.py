from tkinter import  *
import tkinter.messagebox as tmsg # ye module hai tmsg support karta hai
main=Tk()
def help():
    print("i will help you")
    tmsg.showinfo("help","i help you")
def rate():
    print("rate us ")
    value =tmsg.askquestion("was your expericence good","you used this gui ,was your experience good?")
    print(value)
    if value =="yes":
        msg="great,give us star on appstore "
    else:
        msg="tell us what went wrong,we will call you soon"
    tmsg.showinfo("experience",msg)
def divya():
    ans=tmsg.askretrycancel("divya se dosti karlo","sorry divya nahi banegi aapki dost")
    if ans:
        tmsg.showinfo("matlab nahi hai","retry karne pe bhi kuch nahi hoga")
    else:
        tmsg.showinfo("haha","badiya bhai cancel kar diya warna pitte")
main.geometry("700x500")
main.title("menus and submenus in tkinter")
# it is used to make menu in main window
#mymenu=Menu(main)
#mymenu.add_command(label="file")
#mymenu.add_command(label="exit")
#main.config(menu=mymenu)
#main.mainloop()

# it is used to make menu and submenu inside menu
mainmenu=Menu(main)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="new project")
m1.add_command(label="save")
m1.add_separator()
m1.add_command(label="save as")
m1.add_command(label="print")
main.config(menu=mainmenu)
mainmenu.add_cascade(label="file",menu=m1)
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="cut")
m2.add_command(label="copy")
m2.add_separator()
m2.add_command(label="paste")
m2.add_command(label="undo")
main.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="help",command=help)
m3.add_command(label="rate us ",command=rate)
m3.add_command(label="friend divya",command=divya)
mainmenu.add_cascade(label="help",menu=m3)
main.mainloop()