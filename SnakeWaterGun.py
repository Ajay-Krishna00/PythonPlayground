#Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" 
# where players use hand gestures to represent a snake, water, or a gun. 
# The gun beats the snake, the water beats the gun, and the snake beats the water.
#           computer
#           s  w  g
#       s   0  1 -1         1 -win
# user  w  -1  0  1        -1 -lose
#       g   1 -1  0         0 -draw

import random
print("\n\t\t\tWelcome to Snake,Water,Gun\nYou have 10 chances\n")
score=0
i=0
while (i<10):
    choice=input("Enter 's' for snake, 'w' for Water,'g' for Gun\n")
    user_choice=choice.lower()
    l=['s','w','g']
    computer_choice=random.choice(l)
    print(f"The choice of computer is {computer_choice}\n")
    if user_choice ==computer_choice:
        print("Draw!\n")
        score+=0.5
    elif user_choice== 's' and computer_choice=='w':
        print ("You win!\n")
        score+=1
    elif user_choice== 'w' and computer_choice=='g':
        print ("You win!\n")
        score+=1
    elif user_choice== 'g' and computer_choice=='s':
        print ("You win!\n")
        score+=1
    else:print("You Lose\n")
    print(f"your score is {score}")
    i+=1
luck=score*10+5     #Extra 5 marks for running this program :)
print(f"\nYour luck is {luck}%")
