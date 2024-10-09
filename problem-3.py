'''
*******************************
Author:
u3275885
Assignment:
Assessment 2 - Problem 3
4/10/2024
*******************************
'''
try:
    initial = int(input("Starting number of organisms: "))
    rate = int(input("Average daily increase (%): "))
    days = int(input("Number of days to multiply: "))
except ValueError:
    print("Invalid input")
    exit()

# Function to calculate the next day's population
def advance(previous):
    return previous + (previous * (rate / 100))

current = initial
for i in range(days): # Loop through the days
    if i == 0: # If it's the first day, print the initial population
        print(f"Day {i+1}: {current}")
        continue # Skip the rest of the day
    current = advance(current)
    print(f"Day {i+1}: {current}")
