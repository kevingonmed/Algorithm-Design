# 1. Name:
#      -Kevin Gonzalez-
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program calculates the number of days between two dates provided by the user.
#      It validates the input to ensure the dates are valid (e.g., year >= 1753, month between 1 and 12,
#      and day within the valid range for the given month and year). The program also handles leap years
#      correctly and ensures the end date is after the start date. If the input is invalid, the program
# 4. What was the hardest part? Be as specific as possible.
#      - The hardest part was implementing robust input validation. Ensuring the program handled invalid
#      inputs like non-integer years, months outside the range 1–12, and days outside the valid range
#      for each month required careful planning. I also had to ensure the program provided clear error
#      messages and re-prompted the user for valid input.

# 5. How long did it take for you to complete the assignment?
#      -3 hours-



def leap_year(year):
    assert year >= 1753, "Year must be 1753 or later."
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    assert 1 <= month <= 12, "Month must be between 1 and 12."
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if leap_year(year):
        month_days[2] = 29
    return month_days[month]

def is_valid_date(year, month, day):
    if year < 1753:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month(year, month):
        return False
    return True

def days_between(start_day, start_month, start_year, end_day, end_month, end_year):
    assert is_valid_date(start_year, start_month, start_day), "Invalid start date."
    assert is_valid_date(end_year, end_month, end_day), "Invalid end date."
    assert (start_year < end_year) or (start_year == end_year and start_month < end_month) or (start_year == end_year and start_month == end_month and start_day <= end_day), "End date must be after start date."

    if start_year == end_year and start_month == end_month:
        return end_day - start_day
    elif start_year == end_year:
        days = 0
        for month in range(start_month + 1, end_month):
            days += days_in_month(start_year, month)
        days += days_in_month(start_year, start_month) - start_day
        days += end_day
        return days
    else:
        days = days_in_month(start_year, start_month) - start_day
        for month in range(start_month + 1, 13):
            days += days_in_month(start_year, month)
        for year in range(start_year + 1, end_year):
            if leap_year(year):
                days += 366
            else:
                days += 365
        for month in range(1, end_month):
            days += days_in_month(end_year, month)
        days += end_day
        return days

def get_date(prompt):
    while True:
        try:
            year = int(input(f"{prompt} year: "))
            month = int(input(f"{prompt} month: "))
            day = int(input(f"{prompt} day: "))
            if is_valid_date(year, month, day):
                return year, month, day
            else:
                print("Invalid date. Please try again.")
        except ValueError:
            print("Invalid input. Please enter integers.")


"""print("Enter the start date:")
start_year, start_month, start_day = get_date("Start")

print("Enter the end date:")
end_year, end_month, end_day = get_date("End")

print("There are", days_between(start_day, start_month, start_year, end_day, end_month, end_year), "days between the dates.")

"""
def test_days_between():

    test_cases = [

        {
            "input": {"start_year": 1752, "start_month": 1, "start_day": 1, "end_year": 2023, "end_month": 10, "end_day": 5},
            "expected_output": "Invalid start date."
        },

        {
            "input": {"start_year": "abc", "start_month": 1, "start_day": 1, "end_year": 2023, "end_month": 10, "end_day": 5},
            "expected_output": "Invalid input. Please enter integers."
        },

        {
            "input": {"start_year": 2000, "start_month": 0, "start_day": 1, "end_year": 2000, "end_month": 1, "end_day": 1},
            "expected_output": "Invalid start date."
        },

        {
            "input": {"start_year": 2000, "start_month": 13, "start_day": 1, "end_year": 2000, "end_month": 1, "end_day": 1},
            "expected_output": "Invalid start date."
        },

        {
            "input": {"start_year": 2000, "start_month": 1, "start_day": 0, "end_year": 2000, "end_month": 1, "end_day": 1},
            "expected_output": "Invalid start date."
        },

        {
            "input": {"start_year": 2000, "start_month": 2, "start_day": 30, "end_year": 2000, "end_month": 3, "end_day": 1},
            "expected_output": "Invalid start date."
        },

        {
            "input": {"start_year": 2000, "start_month": 1, "start_day": 1, "end_year": 1999, "end_month": 12, "end_day": 31},
            "expected_output": "End date must be after start date."
        },

        {
            "input": {"start_year": 2000, "start_month": 1, "start_day": 1, "end_year": 2000, "end_month": 1, "end_day": 1},
            "expected_output": 0
        },
     
        {
            "input": {"start_year": 2000, "start_month": 1, "start_day": 1, "end_year": 2000, "end_month": 1, "end_day": 31},
            "expected_output": 30
        },

        {
            "input": {"start_year": 2000, "start_month": 1, "start_day": 1, "end_year": 2000, "end_month": 12, "end_day": 31},
            "expected_output": 365
        },

        {
            "input": {"start_year": 2000, "start_month": 12, "start_day": 25, "end_year": 2001, "end_month": 1, "end_day": 8},
            "expected_output": 14
        },

        {
            "input": {"start_year": 2001, "start_month": 10, "start_day": 28, "end_year": 2025, "end_month": 10, "end_day": 5},
            "expected_output": 8743  # Corrected expected output
        }
    ]


    for i, test_case in enumerate(test_cases, 1):
        print(f"Running Test Case {i}...")
        try:

            result = days_between(
                test_case["input"]["start_day"],
                test_case["input"]["start_month"],
                test_case["input"]["start_year"],
                test_case["input"]["end_day"],
                test_case["input"]["end_month"],
                test_case["input"]["end_year"]
            )

            if result == test_case["expected_output"]:
                print(f"Test Case {i}: PASSED")
            else:
                print(f"Test Case {i}: FAILED (Expected: {test_case['expected_output']}, Got: {result})")
        except Exception as e:

            if str(e) == test_case["expected_output"]:
                print(f"Test Case {i}: PASSED")
            else:
                print(f"Test Case {i}: FAILED (Expected: {test_case['expected_output']}, Got: {str(e)})")
        

        print()


test_days_between()