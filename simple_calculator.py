def add(num1,num2):
    return (num1 + num2)

def subtract(num1,num2):
    return (num1 - num2)

def product(num1,num2):
    return (num1 * num2)

def divide(num1,num2):
    if num2==0:
        print("cannot divide by zero\n")
    else:
        return (num1/num2)

def simple_calculator():
    value=True
    while value:
        try:
            num1=float(input("enter 1st number="))
            num2=float(input("enter 2nd number="))
            opt=input("enter operation you want to perform (+,-,*,/) :")
            if opt == "+":
                result = add(num1,num2)
            elif opt == "-":
                result = subtract(num1,num2)
            elif opt == "*":
                result = product(num1,num2)
            elif opt == "/":
                result = divide(num1,num2)
            else:
                print("Invalid operator please choose valid operrations (+,-,*,/)")
            print(f"{num1} {opt} {num2} = {result}")
        except ValueError:
            print("Invalid input")
        
        choice=input("Do you want to perform more calculations (yes/no) :")
        if choice.lower() == "no":
            value = False
            break

simple_calculator()

