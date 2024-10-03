import random
import string

def password_generator():
    try:
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Please enter a valid length.")
            return
        
        print("\nChoose password complexity:")
        print("1. Letters only")
        print("2. Letters and digits")
        print("3. Letters, digits, and symbols")
        
        complexity = int(input("Enter your choice (1/2/3): "))
        
        if complexity == 1:
            characters = string.ascii_letters  
        elif complexity == 2:
            characters = string.ascii_letters + string.digits  
        elif complexity == 3:
            characters = string.ascii_letters + string.digits + string.punctuation  
        else:
            print("Invalid complexity choice.")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"\nGenerated Password: {password}")
    
    except ValueError:
        print("Please enter a valid number.")


password_generator()
