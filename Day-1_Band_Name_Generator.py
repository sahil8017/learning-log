'''
Day 1 - Band Name Generator
Goal: Build a program that creates a band name from user input.

Requirements:

Greet the user with a welcome message.
Ask for the name of the city they grew up in.
Ask for their pet's name.
Combine both answers and print a suggested band name.
'''

print("Welcome to Band Name Generator!")

city = input("What is the name of the city you grew up in?\n")
pet_name = input("What is your pet's name?\n")

print(f"Your Band name could be {city + ' '+ pet_name}")