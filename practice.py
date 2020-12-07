from tkinter import *
import tkinter.messagebox as tmsg
main=Tk()

def success():
    print(namevalue.get(),pricevalue.get())
    with open("order records.txt","w") as f:
        f.write(f"{namevalue.get(),pricevalue.get()}")
    tmsg.showinfo("order received",f"we have received your order of {nameentry.get()} and its price is {priceentry.get()}")

main.geometry("555x555")
main.configure(background="grey")


# heading
Label(main,text="order menu from Aaditya Bhojnalaya",padx=20,pady=15).grid(row=0,column=3)
name=Label(main,text="dish name")
price=Label(main,text="price of dish")
name.grid(row=1,column=2)
price.grid(row=2,column=2)

# creating string variables

namevalue=StringVar()
pricevalue=DoubleVar()
# using entry widget


var=StringVar()
nameentry=Entry(main,textvariable=namevalue)
priceentry=Entry(main,textvariable=pricevalue)
nameentry.grid(row=1,column=3)
priceentry.grid(row=2,column=3)

# creating button to take order
Button(main,text="order",command=success).grid(row=3,column=3)
main.mainloop()
