# 1. Name:
#      Kevin Gonzalez
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -What this program does is open the JSON file and convert it into a dictionary. Using a try-except block, it checks if the file is successfully opened. Afterward, the program asks the user to input their username and password. Then, using if statements, it checks if the entered username exists in the dictionary. Finally, it verifies if the password matches the username, and if so, it prints a message saying the user is authorized to use the system.-
# 4. What was the hardest part? Be as specific as possible.
#      -The hardest part of the assignment was understanding how to access the data within the dictionary, but specifically, the challenge came when I had to compare if the password matched the one associated with the user. This was the most difficult part for me because it required correctly accessing the password in the dictionary using the user’s index. At first, I wasn’t sure how to properly match the password with the correct user, but after a bit of trial and error, I was able to figure it out.-
# 5. How long did it take for you to complete the assignment?
#      -Approximately 3 hours and 30 minutes- 

import json

# Try to open the Lab02.json file
try:
    with open("Lab02.json", "r") as file:
        data = file.read()  # Read the content of the file
        data2 = json.loads(data)  # Convert the file data into a dictionary
        

# If the file cannot be opened, print an error message
except OSError:
    print("Unable to open file Lab02.json.")

# Prompt the user to input their username and password
index_ussername = input("Username: ")
index_password = input("Password: ")

# Check if the entered username exists in the dictionary (in the "username" list)
if index_ussername in data2["username"]:
    # Find the index of the username in the list
    user_index = data2["username"].index(index_ussername) 
    
    # Check if the entered password matches the password at the same index in the "password" list
    if index_password == data2["password"][user_index]:
        print("You are authenticated!")  # If the password matches, print authentication success
    else:
        print("You are not authorized to use the system.")  # If the password doesn't match, print an error message
else:
    print("You are not authorized to use the system.")  # If the username is not found, print an error message



