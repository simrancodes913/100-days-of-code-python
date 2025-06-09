size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N:").lower()
bill=0
if size=="s":
    bill+=15
elif size=="m":
    bill+=20
elif size=="l":
    bill+=25
else:
    print("You entered a wrong option.")
if pepperoni=="y":
    if size=="s":
       bill+=2
    else:
       bill+=3
else:
    bill+=0
if extra_cheese=="y":
    bill+=1
else:
    bill+=0
print("Welcome to Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}.")