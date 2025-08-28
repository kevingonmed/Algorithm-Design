# 1. Name:
#      Kevin Gonzalez
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program asks the user to provide a JSON file, reads the file to get a list of values, and sorts the list in descending order using the Selection Sort method. Once sorted, it shows the sorted list to the user. The program checks that the file is valid, the list is not empty, and the data is in the correct format before sorting.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was sorting the elements in order and creating the loop to make it work, because whenever I tried, I would either get an error or the list would be sorted in a different way. But after doing that and using some asserts, I was able to realize what I was doing wrong.
# 5. How long did it take for you to complete the assignment?
#      Between 2:30 and 3 hours

import os
import json

def selection_sort():
    # Input the file name
    file_name = input("What is the name of the file?: ")
    assert file_name, "Error: File name cannot be empty."

    # Open and read the file
    assert os.path.exists(file_name), f"Error: The file {file_name} does not exist."
    with open(file_name, "r") as file:
        names_text = file.read()
        assert names_text.strip(), f"Error: The file {file_name} is empty."
        try:
            names_json = json.loads(names_text)
        except json.JSONDecodeError:
            print(f"Error: The file {file_name} contains invalid JSON.")
            exit(1)
        assert names_json, "Error: Failed to parse JSON data."

        assert "array" in names_json, "Error: The 'array' key is missing in the JSON data."
        names_list = names_json["array"]

    assert len(names_list) > 0, "Error: The 'array' in the JSON file is empty."
    i_max = len(names_list) - 1

    # Selection Sort algorithm
    for i_pivot in range(i_max):
        assert i_pivot <= i_max, "Error: Pivot index exceeds the maximum index."
        i_largest = i_pivot
        assert 0 <= i_largest <= i_max, "Error: The i_largest index is out of bounds."

        for i_check in range(i_pivot + 1, len(names_list)):
            assert i_check <= len(names_list), "Error: Check index exceeds list length."
            # We want the largest element, so compare if the current element is greater
            if names_list[i_check] < names_list[i_largest]:
                i_largest = i_check

        names_list[i_largest], names_list[i_pivot] = names_list[i_pivot], names_list[i_largest]

    # Print the sorted list
    print("Sorted list of names:")
    assert len(names_list) > 0, "Error: The list to print is empty."
    for name in names_list:
        print(f"\t{name}")
        assert isinstance(name, str), "Error: The name is not a string."

# Call the function
selection_sort()