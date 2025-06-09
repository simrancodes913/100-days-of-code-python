print("Welcome to the tip calculator!")
a=int(input("What was the total bill?"))
b=int(input("How much tip would you like to give?[10,12 or 15]"))
c=int(input("How many people to split the bill?"))
d=a*(1+(b/100))/c
print(f"Each person should pay: {d}")
print(round(d))