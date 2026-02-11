#user credntials creation script with 16 to 25 characters and special character for the password requirements
def user_account_creation():
    user_input = input("Enter your name here: ")
    print(f"Hello, {user_input}!")

    user_id_input = input("Your id must be within the range of 30 charcaters:: ")
    while True:
        if len(user_id_input) > 30: # Check if ID is within 30 characters or less
            print("Error: ID exceeds 30 characters.")
            user_id_input = input("Please enter a valid ID (within 30 characters), try again.: ")
        else:
            print(f"Your ID is: {user_id_input}")
            break # Exit the loop if the ID is valid
    
    user_password = input("Enter your password here, it must be 25 characters or less: ") 
    while True:
        if len(user_password) < 16 or len(user_password) > 25: # Check if password is between 16 and 25 characters long
            print("Error: Password must be exactly 25 characters including special characters, please try again.")
            user_password = input("Please enter a valid password (exactly 25 characters): ")
        elif not any(c in "!@#$%^&*()-+" for c in user_password): # Check for at least one special character
            print("Error: Password must contain at least one special character.")
            user_password = input("Please enter a valid password (exactly 25 characters with special character): ")
        elif user_password == user_id_input:
            print("User ID and passsword can not be the same, please try again.")
        else:
            print("Password accepted.")
            break # Exit the loop if the password is valid
    print("Account creation successful!")
user_account_creation() #im calling back the function to run the program