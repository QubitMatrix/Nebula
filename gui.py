from tkinter import *
import ale1

root=Tk()
root.title("Nebula")
root.wm_geometry("1380x300")
root.resizable(width=False,height=False)
bs=Text(root,height=3,width=130,bg="black",fg="cyan",font="ds-digital 13",)
bs.pack()
bs.insert(INSERT,"Nebula is the personal assistant for your pc. The program is based on voice commands and it returns output also as voice.")
bs.insert(END,"\nHere are the list of functions it can perform")
l1=Entry(root,width=170,bg="black",fg="white")
l1.insert(0,"l")
l1.place(x=0,y=150)
def scr():
    l1.delete(0, END)
    l1.insert(0,"Screenshot is the module that takes a screenshot of the screen at the time of the command. It is stored in the screenshots folder within the same directory")
def cam():
    l1.delete(0,END)
    l1.insert(0,"This opens the webcam and takes a picture when letter 'q' is pressed. It is stored in the pictures folder within the same directory")
def tim():
    l1.delete(0,END)
    l1.insert(0,"Tells the time at the current moment")
def webt():
    l1.delete(0,END)
    l1.insert(0,"Opens the given url at the given time and brings the opened tab to highlight")
def zoo():
    l1.delete(0,END)
    l1.insert(0,"Opens the zoom website and joins the meeting with the given id and password at the given time")
def pla():
    l1.delete(0,END)
    l1.insert(0,"It plays the first video in youtube under the given command search(like play happy birthday)")
def wha():
    l1.delete(0,END)
    l1.insert(0,"Sends given message on whatsapp to the given number(scheduled or instant)")
def shu():
    l1.delete(0,END)
    l1.insert(0,"Can shutdown or restart according to command given")
def ope():
    l1.delete(0,END)
    l1.insert(0,"Can open a new notepad file")
def rem():
    l1.delete(0,END)
    l1.insert(0,"Sets a reminder to do a specified work at a specified time")
def exi():
    root.destroy()
    ale1.run()
b1=Button(root,text="Screenshot",command=scr)
b1.place(x=1015,y=85)
b2=Button(root,text="Camera",command=cam)
b2.place(x=130,y=85)
b3=Button(root,text=" The time",command=tim)
b3.place(x=210,y=85)
b4=Button(root,text="Website timer",command=webt)
b4.place(x=300,y=85)
b5=Button(root,text="Zoom timer",command=zoo)
b5.place(x=430,y=85)
b6=Button(root,width=10,text="Play",command=pla)
b6.place(x=1120,y=85)
b7=Button(root,text="whatsapp",command=wha)
b7.place(x=635,y=85)
b8=Button(root,text="shutdown/restart",command=shu)
b8.place(x=730,y=85)
b9=Button(root,text="open notepad",command=ope)
b9.place(x=885,y=85)
b11=Button(root,text="Reminder",command=rem)
b11.place(x=540,y=85)
ll=Label(root,bg="black",fg="white",font="consolas 10")
ll.place(x=10,y=200)
ll.config(text="Click here if the introduction is clear and you want to proceed to the voice module")
b10=Button(root,text="Click here",command=exi)
b10.place(x=10,y=230)

root.mainloop()

