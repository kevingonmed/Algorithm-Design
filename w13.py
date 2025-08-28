# 1. Name:
#      Kevin Gonzalez
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This program is designed to read a JSON file containing an array of integers. The goal is to calculate the maximum average of any contiguous sub-array of size n, where n is a user-provided value. The program begins by validating the input file and ensuring it is in JSON format and contains a list of integers under the key "array". After that, the program computes the sum of the first n elements and then slides a window of size n across the array to find the maximum sum. Finally, it calculates and prints the average of the sub-array with the maximum sum.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was handling edge cases and ensuring that the program could deal with invalid or malformed input files. For example, ensuring that the program correctly handles situations where the file is missing, the format is incorrect, or the JSON does not contain the expected key ("array") required for processing.
# 5. How long did it take for you to complete the assignment?
#      -2 hours-
 
import json

# Function to process each test case
def process_file(filename, n):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file {filename} is not in JSON format.")
        return

    # Validate the JSON
    if "array" not in data:
        print(f"Error: The file {filename} must contain the 'array' key.")
        return

    array = data["array"]

    # Validate that it is a list of integers
    if not isinstance(array, list) or not all(isinstance(x, int) for x in array):
        print(f"Error: 'array' in {filename} must be a list of integers.")
        return

    if n <= 0 or n > len(array):
        print(f"Error: The size must be positive and not greater than the size of the array in {filename}.")
        return

    # Pseudocode section
    # sum = data[0] + data[1] + ... + data[n-1]
    sum = 0
    for i in range(n):
        sum += array[i]

    sum_largest = sum

    # Sliding window
    for i_remove in range(len(array) - n):
        i_add = i_remove + n
        sum = sum - array[i_remove] + array[i_add]
        if sum > sum_largest:
            sum_largest = sum

    # Show result
    print(f"Maximum average for {filename}: {sum_largest / n}")


# Define test cases (filename and sub-array size n)
test_cases = [
    ("banana.txt", 0),        # Bad file
    ("small.json", 1000),     # Bad subset
    ("small.json", 10),       # Small subset
    ("large.json", 100),      # Large subset
]

# Run the test cases
for filename, n in test_cases:
    process_file(filename, n)


