print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $ "))
people = int(input("How many people are splitting the bill? "))
tip_percentage = int(input("How much would you like to tip? 10, 12 or 15? "))

total_bill = bill * (1 + tip_percentage / 100)
bill_per_person = total_bill / people

print(f"Each person should pay: ${bill_per_person:.2f}")
