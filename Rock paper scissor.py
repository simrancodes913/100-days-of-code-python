import random
game_images=[rock,paper,scissors]
user_choice= int(input("what do u choose?type 0 for rock,1 for paper and 2 or scissors"))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])
computer_choice=random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])
if user_choice==0 and computer_choice==2:
    print("You win!")
elif user_choice >= 3 or user_choice < 0:
    print("You have entered an invalid number.You lose!")

elif computer_choice==0 and user_choice==2:
    print("You lose!")
elif computer_choice>user_choice:
    print("You lose!")
elif user_choice>computer_choice:
    print("you win!")
elif computer_choice==user_choice:
    print("Match draw!")
else:
    print("")
