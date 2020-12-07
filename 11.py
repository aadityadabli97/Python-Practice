# concept of canvas widget(canvas widget is used to draw any shape)
from tkinter import *
main=Tk()
main.title("aaditya ki design")
canvas_width=800
canvas_height=400
main.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(main,width=canvas_width,height=canvas_height)
can_widget.pack()
#the line goes from x1,y1 to x2,y2
can_widget.create_line(0,0,800,400,fill="red")

# to create a rectangle specify coordinates in this order -coordinates of top left and coordinates of right bottom
can_widget.create_rectangle(10,10,500,500,fill="yellow")
can_widget.create_text(400,200,text="python")
can_widget.create_oval(50,50,100,100,fill="grey")
main.mainloop()