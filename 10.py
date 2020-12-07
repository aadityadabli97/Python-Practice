from tkinter import *
main=Tk()
def getvalue():
    print("successfully registered ")

    print(f"{namevalue.get(),emailvalue.get(),passwordvalue.get(),termsvalue.get()}")
    with open("records.txt","w")as f: #aisa karne se ek nayi file ban jati hai jaisa is case me records.txt ban gayi hai
#yaha w means file written mode me hai,r hota to read mode me hoti,a hota to append mode me hoti
        f.write(f"{namevalue.get(),emailvalue.get(),passwordvalue.get(),termsvalue.get()}") #isse file me ye sab values
# write ho jaegi ,file me bas ek hi value ko write karwa sakte hai bina f string use kare
main.geometry("600x600")
# heading
Label(text="welcome to my site , Register here!!", font="verdana", padx=15,pady=15).grid(row=0, column=3)
# text for our site
name = Label(main, text="name")
email = Label(main, text="email")
password = Label(main, text="password")

# pack text for our site using grid function(we can also use grid function to pack)

name.grid(row=1,column=2)
email.grid(row=2, column=2)
password.grid(row=3, column=2)
# tkinter variable for storing entries

namevalue = StringVar()
emailvalue = StringVar()
passwordvalue = StringVar()
termsvalue = IntVar()

# entries for ous site

nameentry = Entry(main, textvariable=namevalue)
emailentry = Entry(main, textvariable=emailvalue)
passwordentry = Entry(main, textvariable=passwordvalue)

# packing the entries
nameentry.grid(row=1, column=3)
emailentry.grid(row=2, column=3)
passwordentry.grid(row=3, column=3)

# checkbox
terms = Checkbutton(text="are you agree with our terms and conditions", variable=termsvalue)
terms.grid(row=4, column=3)

# button and packing it and assigning it to a command
Button(text="register ",command=getvalue).grid(row=5,column=2)
main.geometry("500x500")
main.mainloop()