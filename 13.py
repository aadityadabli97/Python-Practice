from tkinter import*
main=Tk()
main.geometry("700x500")
main.title("menus and submenus in tkinter")
'''it is used to make menu in main window
mymenu=Menu(main)
mymenu.add_command(label="file")
mymenu.add_command(label="exit")
main.config(menu=mymenu)
main.mainloop()'''

# it is used to make menu and submenu inside menu 
mainmenu=Menu(main)  # yaha mainmenu ek menu ban gaya main window me
m1=Menu(mainmenu,tearoff=0)  # m1 ek submenu hai jo mainmenu ke andar ban gaya
m1.add_command(label="new project")
m1.add_command(label="save")
m1.add_separator()
m1.add_command(label="save as")
m1.add_command(label="print")
main.config(menu=mainmenu)
mainmenu.add_cascade(label="file",menu=m1)# yaha mainmenu banaya jiska name file hai or uske andar m1 ko cascade kar diya
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="cut")
m2.add_command(label="copy")
m2.add_separator()
m2.add_command(label="paste")
m2.add_command(label="undo")
main.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)
main.mainloop()