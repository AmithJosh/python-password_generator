import random
import string

def generate_password(length):
    """Generate a random password."""
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choice()
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main part of the script
if __name__ == "__main__":
    try:
        # Get the desired password length from the user
        length = int(input("Enter the desired length of the password: "))
        
        # Check if the length is a positive number
        if length > 0:
            new_password = generate_password(length)
            print(f"Your new password is: {new_password}")
        else:
            print("Please enter a positive number for the password length.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")