# connecting scrollbar to the text
from tkinter import  *
main=Tk()
main.geometry("500x500")
''' for  connecting scrollbar to a widget 
1> widget(yscrollcommand=scrollbar.set)
2> scrollbr.config(command=widget.yview)  
 these 2 commands are require '''

'''listbox=Listbox(main)
for i in range(100):
    listbox.insert(END,f"item{i}")           # can be use alternatively for learning purpose
listbox.pack()
main.mainloop()'''

# now we are connecting scrollbar to our text
'''scrollbar=Scrollbar(main)
scrollbar.pack(side=RIGHT,fill=Y)

listbox=Listbox(main,yscrollcommand=scrollbar.set)

for i in range(100):
    listbox.insert(END,f"item{i}")
listbox.pack(fill="both")
scrollbar.config(command=listbox.yview)
main.mainloop()'''

#simple notepad
scrollbar=Scrollbar(main)
scrollbar.pack(side=RIGHT,fill=Y)
text=Text(main,yscrollcommand=scrollbar.set)
text.pack(fill="both")
scrollbar.config(command=text.yview)
main.mainloop()
