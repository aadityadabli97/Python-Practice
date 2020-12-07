# concept of sliders in tkinter
from tkinter import *
main=Tk()
main.geometry("500x500")
main.title("concept of sliders in tkinter using scale()")
myslider=Scale(main,from_=0,to=100) # slider ko main window me pack karna padta hai or range deni padti hai uski
myslider2=Scale(main,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(30)
myslider.pack()
myslider2.pack()

main.mainloop()