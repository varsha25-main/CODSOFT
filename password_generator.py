import secrets
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits  
    symbols = string.punctuation
    characters = letters + digits + symbols
    list=[]
    for i in range(length):
        list += secrets.choice(characters)
    print(list)
    secrets.SystemRandom().shuffle(list)
    password = ""
    for i in range(length):
        password += list[i]
    return password

value = True
while value:
    try:
        length = int(input("Enter the length of the password: "))
        if length < 4:
            print("Password length must be at least of 4 for a strong password.")
            continue
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    
    choice = input("Do you want to generate another password (yes/no): ")
    if choice.lower() == "no":
        value = False
        break
    
