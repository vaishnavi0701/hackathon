from tkinter import*
import random
Var=Tk()
Var.geometry("800x700")
Var.resizable(0,0)
Var.title("dataflair-rock,paper,scissor")
Var.config(bg="yellow")
user_take=StringVar()
Label(Var,text="choose any one:rock,paper,scissor",font="arial 15 bold",bg="black")
Entry(Var,font="bold 30",textvariable=user_take,bg="antiquewhite2").place(x=90,y=60)
com_pack=random.randint(1,3)
if com_pack==1:
    com_pack="rock"
elif com_pack==2:
    com_pack="paper"
else:
    com_pack="scissor"
result=StringVar()
def play():
    user_pack=user_take.get()
    if user_pack==com_pack:
        result.set("tie,you both select same")
    elif user_pack=="rock" and com_pack=="paper":
        result.set("you lose,computer select paper")
    elif user_pack=="rock" and com_pack=="scissor":
        result.set("you win,computer select scissor")
    elif user_pack=="paper" and com_pack=="scissor":
        result.set("you lose,computer select scissor")
    elif user_pack=="paper" and com_pack=="rock":
        result.set("you win,computer select rock")
    elif user_pack=="scissor" and com_pack=="rock":
        result.set("you lose,computer select rock")
    elif user_pack=="scissor" and com_pack=="paper":
        result.set("you win,computer select paper")
    else:
        result.set("invvaid: choose any one rock,paper,scissor")
def reset():
    result.set("")
    user_take.set("")
def exit():
    Var.destroy()

Entry(Var,font="arial 10 bold",textvariable=result,bg="antiquewhite2",width=50).place(x=25,y=250)
Button(Var,font="arial 13 bold",text="PLAY",padx=5,bg="white",command=play).place(x=250,y=150)
Button(Var,font="arial 13 bold",text="RESET",padx=5,bg="white",command=reset).place(x=70,y=310)
Button(Var,font="arial 13 bold",text="EXIT",padx=5,bg="white",command=exit).place(x=230,y=310)



Var.mainloop()


