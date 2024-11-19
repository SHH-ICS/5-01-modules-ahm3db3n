import random

def Q2RandomRange():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    lower = min(num1, num2)
    upper = max(num1, num2)
    random_number = random.randint(lower, upper)
    print(f"A random number between {lower} and {upper} is: {random_number}")

Q2RandomRange()
