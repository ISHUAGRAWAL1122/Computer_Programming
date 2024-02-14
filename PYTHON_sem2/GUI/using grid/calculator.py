from tkinter import *
class greet:
    def __init__(self,main_win):
        
        self.main_win=main_win
        self.main_win.geometry('300x400')
        self.main_win.title("Sum of two")
        self.main_win.minsize(400,400)
        self.main_win.maxsize(400,400)
        self.s=""
        Label(self.main_win,text="CALCULATOR",font=29,justify='center').grid(row=0,column=0)
        self.lb1=Label(self.main_win,text="",font=29)
        self.lb1.grid(row=1,column=0,sticky=W,padx=20,pady=15)
        Button(self.main_win,text="C",command=self.clr,font=27).grid(row=2,column=0,ipady=10,ipadx=10)
        Button(self.main_win,text="^",command=self.ope("^"),font=27).grid(row=2,column=1,ipady=10,ipadx=10)
        Button(self.main_win,text="&",command=self.ope("&"),font=27).grid(row=2,column=2,ipady=10,ipadx=10)
        Button(self.main_win,text="|",command=self.ope("|"),font=27).grid(row=2,column=3,ipady=10,ipadx=10)
        Button(self.main_win,text="/",command=self.ope("/"),font=27).grid(row=3,column=3,ipady=10,ipadx=10)
        Button(self.main_win,text="*",command=self.ope("*"),font=27).grid(row=4,column=3,ipady=10,ipadx=10)
        Button(self.main_win,text="-",command=self.ope("-"),font=27).grid(row=5,column=3,ipady=10,ipadx=10)
        Button(self.main_win,text="+",command=self.ope("+"),font=27).grid(row=6,column=3,ipady=10,ipadx=10)
        Button(self.main_win,text="7",command=self.nm(7),font=27).grid(row=3,column=0,ipady=10,ipadx=10)
        Button(self.main_win,text="8",command=self.nm(8),font=27).grid(row=3,column=1,ipady=10,ipadx=10)
        Button(self.main_win,text="9",command=self.nm(9),font=27).grid(row=3,column=2,ipady=10,ipadx=10)
        Button(self.main_win,text="4",command=self.nm(4),font=27).grid(row=4,column=0,ipady=10,ipadx=10)
        Button(self.main_win,text="5",command=self.nm(5),font=27).grid(row=4,column=1,ipady=10,ipadx=10)
        Button(self.main_win,text="6",command=self.nm(6),font=27).grid(row=4,column=2,ipady=10,ipadx=10)
        Button(self.main_win,text="1",command=self.nm(1),font=27).grid(row=5,column=0,ipady=10,ipadx=10)
        Button(self.main_win,text="2",command=self.nm(2),font=27).grid(row=5,column=1,ipady=10,ipadx=10)
        Button(self.main_win,text="3",command=self.nm(3),font=27).grid(row=5,column=2,ipady=10,ipadx=10)
        Button(self.main_win,text="0",command=self.nm(0),font=27).grid(row=6,column=0,ipady=10,ipadx=10)
        Button(self.main_win,text="=",command=self.res,font=27).grid(row=6,column=1,columnspan=2,ipady=10,ipadx=10)
       
    def res(self):
        self.st.config((self.st.get()))
    def ope(self,optr):
        self.st.config(str(self.st.get())+str(optr))
    def nm(self,num):
        self.st.config(str(self.st.get())+str(num))
    def clr(self):
        self.st.config("")
        
root=Tk()
exe=greet(root)
root.mainloop()
