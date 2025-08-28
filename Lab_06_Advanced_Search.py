# 1. Name:
#      Kevin Gonzalez
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program opens the file specified by the user and then prompts the user to enter a word they are searching for in the JSON file. It then checks if the word exists in the array. If it is found, the program displays a "found" message, and if it is not found, it displays a "not found" message.
# 4. Algorithmic Efficiency
#      -I think that is O(log n), where n is the number of elements in the array. This is because each step halves the search range, making it efficient for large datasets.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was implementing the while loop to return the correct result. Additionally, the last if statement was confusing at times, as it occasionally gave me results I didn’t expect. However, after initializing the variables correctly and making a few adjustments, I was able to get the expected results.
# 6. How long did it take for you to complete the assignment?
#      3 hours  

import os
import json

# Input the file name
file_name = input("What is the name of the file?: ")

# Open and read the file
with open(file_name, "r") as file:
    names_text = file.read()
    names_json = json.loads(names_text)
    names_list = names_json["array"]

# Input the element to search for
element = input("What are we looking for?: ")

# Initialize variables 
i_first = 0
i_last = len(names_list) - 1  # Corrected to len(names_list) - 1
found = False

# Search loop
while i_first <= i_last:
    i_middle = (i_first + i_last) // 2

    if names_list[i_middle] < element:
        i_first = i_middle + 1
    elif names_list[i_middle] > element:
        i_last = i_middle - 1
    else:
        found = True
        break

# Check if the element was found and print the appropriate message
if found:
    print(f"We found {element} in {os.path.basename(file_name)}")
else:
    print(f"We could not find {element} in {os.path.basename(file_name)}")