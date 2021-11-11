
from tkinter import*
from random import randint
from tkinter import ttk
varieble=Tk()
varieble.title("WINDOW GAME")
label=Label(varieble,font=("bold",30),text="rock,paper,scissor-game",bg="pink",fg="black")
label.pack()
varieble.geometry("900x900+300+100")
#varieble.resizable(0,0)
# root.mainloop()
paper=PhotoImage(file="/home/vinaata/Desktop/p.png")
rock=PhotoImage(file="/home/vinaata/Desktop/stone.png")
scissor=PhotoImage(file="/home/vinaata/Desktop/scissor.png")
# varieble.mainloop()

image_list=[paper,rock,scissor]
pick_number=randint(0,2)

image_label=Label(varieble,image=image_list[pick_number],bd=0)
image_label.pack(pady=20)




# spin function
def spin():
    pick_number=randint(0,2)
    image_label.config(image=image_list[pick_number])

# user_choice=ttk.Combobox(varieble,values="paper","rock","scissor")





varieble.mainloop()



    

# while True:
#     player_choice = input('What do you pick? (rock, paper, scissors)')
#     player_choice.strip()
#     random_moves = randint(0, 2)
#     moves = ['rock', 'paper', 'scissors']
#     computer_choice = [random_moves]
#     print(computer_choice)

#     if player_choice == computer_choice:
#         print('choice your option')
#     elif player_choice  == 'rock' or computer_choice == 'scissors':
#         win()
#     elif player_choice  == 'paper' or computer_choice == 'scissors':
#         lose()
#     elif player_choice == 'scissors' or computer_choice == 'paper':
#         win()
#     elif player_choice == 'scissors' or computer_choice == 'rock':
#         lose()
#     elif player_choice == 'paper' or computer_choice == 'rock':
#         win()
#     elif player_choice == 'rock' and computer_choice == 'paper':
#         lose()
#     again = input('Do you want to play again? (y or n)').strip()
#     if again == 'n':
#         break
    


player__choice=ttk.Combobox(varieble,value=("rock","paper","scissor"))
player__choice.current(0)
player__choice.pack(pady=50)


# spin button

spin_button=Button(varieble,text="spin!",command=spin)
spin_button.pack(pady=10)


varieble.mainloop()

























# from tkinter import*

# root=Tk()

# canvas=canvas(width==400,hight==250,bg=black)
# canvas.pack()

# photo=PhotoImage(file="//home//vinaata/Desktop//p.png")
# canvas.create_image(20,20, Image=photo,anchor=centeral)

# root.mainloop()

