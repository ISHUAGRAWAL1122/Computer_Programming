from tkinter import *

root = Tk()

def rest():
    for i in b_l:
        i.config(text=" ")

b1 = Button(root, text="", font=69, bg='white', height=5, width=9)
b2 = Button(root, text="", font=69, bg='white', height=5, width=9)
b3 = Button(root, text="", font=69, bg='white', height=5, width=9)
b4 = Button(root, text="", font=69, bg='white', height=5, width=9)
b5 = Button(root, text="", font=69, bg='white', height=5, width=9)
b6 = Button(root, text="", font=69, bg='white', height=5, width=9)
b7 = Button(root, text="", font=69, bg='white', height=5, width=9)
b8 = Button(root, text="", font=69, bg='white', height=5, width=9)
b9 = Button(root, text="", font=69, bg='white', height=5, width=9)

b_l = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

b10 = Button(root, text="reset", command=rest)
b10.grid(row=3, column=1,ipadx=27,pady=7)


b5.config(text="⭕", font=69,fg="red")

b1.config(text="❌",fg="Blue")

root.mainloop()
