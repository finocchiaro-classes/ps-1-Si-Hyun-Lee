# Ask the user for the first number, store the value in a variable


# Ask the user for the second number, store the value in a variable


# Repeat back the numbers


# Perform calculations. Be careful about string formatting for autograders.

firstnum = int(input("Enter an intfeger between 10 and 100: "))
secondnum = int(input("Enter an integer less than 4: "))

print(f"You entered {firstnum} and {secondnum}")
print(f"{firstnum} + {secondnum} = {firstnum + secondnum}")
print(f"{firstnum} * {secondnum} = {firstnum * secondnum}")
print(f"{firstnum} ** {secondnum} = {firstnum ** secondnum}")
print(f"{firstnum} % {secondnum} = {firstnum % secondnum}")
