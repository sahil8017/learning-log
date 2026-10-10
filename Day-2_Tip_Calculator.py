'''
Day 2 - Tip Calculator
Goal: Work out how much each person should pay when splitting a bill with a tip.

Requirements:

Ask for the total bill amount (may be a decimal, e.g. 150.50).
Ask how much tip to give: 10, 12, or 15 (as a whole number percent).
Ask how many people are splitting the bill.
Calculate each person's share = (bill + bill * tip%) / people.
Print the result formatted to 2 decimal places.
'''

print("Welcome to the Tip Calculator!\n")
bill_amount = float(input("What was the total bill? "))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How much people to split the bill? "))

print(f"Each person should pay: {(bill_amount + bill_amount * (tip_amount / 100)) / people}")