from tkinter import *
from tkinter import messagebox
import random
class tictactoe:
    def __init__(self,root):
        self.root=root
        self.root.maxsize(280,373)
        self.sign=["⭕","❌"]
        self.temp="⭕"
        self.l=Label(root,text="Tic-Tac-Toe",font=13)
        self.l.grid(row=0,column=1)
        self.b1 = Button(root, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b1,0))
        self.b2 = Button(root, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b2,1))
        self.b3 = Button(root, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b3,2))
        self.b4 = Button(root, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b4,3))
        self.b5 = Button(root, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b5,4))
        self.b6 = Button(root, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b6,5))
        self.b7 = Button(root, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b7,6))
        self.b8 = Button(root, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b8,7))
        self.b9 = Button(root, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b9,8))

        self.b_v = [self.b1.cget("text"), self.b2.cget("text"), self.b3.cget("text"), self.b4.cget("text"),\
                     self.b5.cget("text"), self.b6.cget("text"), self.b7.cget("text"), self.b8.cget("text"), self.b9.cget("text")]
        self.b_l=[self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9]
        self.b1.grid(row=1, column=0)
        self.b2.grid(row=1, column=1)
        self.b3.grid(row=1, column=2)
        self.b4.grid(row=2, column=0)
        self.b5.grid(row=2, column=1)
        self.b6.grid(row=2, column=2)
        self.b7.grid(row=3, column=0)
        self.b8.grid(row=3, column=1)
        self.b9.grid(row=3, column=2)

        self.b10 = Button(root, text="reset", command=self.rst)
        self.b10.grid(row=4, column=0,columnspan=3,ipadx=60,pady=7)

    def rst(self):
        self.l.config(text="Tic-Tac-Toe",fg="black")
        for i in self.b_l:
            i.config(text="")
        self.b_v = [self.b1.cget("text"), self.b2.cget("text"), self.b3.cget("text"), self.b4.cget("text"),\
                     self.b5.cget("text"), self.b6.cget("text"), self.b7.cget("text"), self.b8.cget("text"), self.b9.cget("text")]
    def btnclk(self,bp,b_index):
        s=bp.cget("text")
        if s=="":
            if self.temp=="⭕":
                si=self.sign[1]
                self.temp=self.sign[1]
            elif self.temp=="❌":
                si=self.sign[0]
                self.temp=self.sign[0]
            bp.config(text=si,fg="red")
            self.b_v[b_index]=si
            if (self.b_v[0]==self.b_v[1]==self.b_v[2]==si)  or (self.b_v[0]==self.b_v[3]==self.b_v[6]==si) or \
                (self.b_v[2]==self.b_v[5]==self.b_v[8]==si) or (self.b_v[3]==self.b_v[4]==self.b_v[5]==si) or \
                (self.b_v[6]==self.b_v[7]==self.b_v[8]==si) or (self.b_v[0]==self.b_v[4]==self.b_v[8]==si) or \
                (self.b_v[2]==self.b_v[4]==self.b_v[6]==si) or (self.b_v[1]==self.b_v[4]==self.b_v[7]==si) :
                self.l.config(text=si+" win",fg="Blue")
                print(si,"win")
                messagebox.showinfo("win",si+" win")
                self.rst()
            c=0
            for i in self.b_v:
                if i in self.sign:
                    c=c+1
            if c==9:
                self.l.config(text="Try Again",fg="red")
                messagebox.showinfo("Better Luck Next Time","It's a Tie")
                self.rst()
root = Tk()
exe=tictactoe(root)
root.mainloop()
