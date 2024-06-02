def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print("""
select operation
1. Add
2. Subtract
3. Multiply
4. divide
""")


while True:
    choice = input("enter choice(1 / 2 / 3 / 4)")
    if choice in ("1", "2" , "3" , "4" ):
        num1 = float(input("Please enter the first number"))
        num2 = float(input("Please enter the second number"))
        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        if choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        if choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        if choice == "4":
            print(f"{num1} / {num2} = {divide(num1, num2)}")

    else:
        print("Invalid input")