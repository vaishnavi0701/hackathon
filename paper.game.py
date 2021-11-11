
from tkinter import*
from random import randint
from tkinter import ttk
varieble=Tk()
varieble.title("WINDOW GAME")
label=Label(varieble,font=("bold",30),text="rock,paper,scissor-game",bg="pink",fg="black")
label.pack()
varieble.geometry("900x900+300+100")
varieble.resizable(0,0)
# root.mainloop()
paper=PhotoImage(file="/home/vinaata/Desktop/p.png")
rock=PhotoImage(file="/home/vinaata/Desktop/stone.png")
scissor=PhotoImage(file="/home/vinaata/Desktop/scissor.png")
# varieble.mainloop()

image_list=[paper,rock,scissor]
pick_number=randint(0,2)

image_label=Label(varieble,image=image_list[pick_number])
image_label.pack(pady=20)
