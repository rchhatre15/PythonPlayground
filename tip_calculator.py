print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
percentage = float(input("What percent tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
print(f"Each person should pay ${round(((total + total * percentage / 100) / people), 2)}")