


from cgitb import text
from tkinter import *
from turtle import width
window=Tk()
window.title("my awesome app")
window.configure(bg='red')
window.geometry("400x400")#fix the window size
f_name=Label(window,text="First name",font=("arial Bold",50))
s_name=Label(window,text="second name",font=("arial Bold",50))
f_name.grid(column =60,row= 100)
s_name.grid(column =60,row= 120)
def open_popup():
    top=Toplevel(window)
    top.geometry("200x200")
    top.title("pop up window")
    top.configure(bg='green')
    msg=Label(top,text="welcome to popup",font=("150x150"))
btn=Button(window,text="click me")
btn.grid(column =120,row= 150)
txt_box=Entry(window,width =10)
txt_box.grid(column =100,row =70)
window.mainloop()