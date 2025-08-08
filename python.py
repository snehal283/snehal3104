
'''#1. input from user (rock,paper,sisor)
#2.computer choice(computer will choose randomly not conditionally)
#3. Result

#cases:
# A-rock
rock-rock = tie
Rock - paper = paper win
rock - scissor = Rock win


B- paper
paper-paper = tie
paper- rock = ppaer win
paper- scissor = sissor win


C- scissor
scissor- scissor= tie
scissor- rock = rock win
scissor-paper=scissor win

'''
import random # random module
item_list = ["Rock", "Paper", " Scissor"]

User_choice = input("Enter your move =Rock , Paper , Scissor :")
comp_choice = random.choice(item_list)

print(f"User_choice = { User_choice}, Computer choice = {comp_choice}" )

if User_choice == comp_choice:
    print("Both Chooses same: = Match tie")

elif User_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock ,Computer win")
    else:
        print("Rock Smashes Scissor , you win ")
    
elif User_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper , Computer win")
    else:
        print("Paper cover Rock , You win")


elif User_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper ,  you win")
    else:
        print("Rock Smashes scissor, computer win")
        