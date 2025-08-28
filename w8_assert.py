"Asserts in Class"
def average_gpa(gpas):  
    ''' Find the average GPA from the list '''
    assert isinstance(gpa, float)#type malo
    assert len(gpas) > 0
    # Add them up.
    sum = 0
    for gpa in gpas:
        sum += gpa
        assert gpa >= 0
        assert gpa <= 4.0
    # Compute the average and return.
    average = sum / len(gpas)
    assert average >= 0
    assert average <= 4.0
    return average

print(average_gpa(["2.0", 3.0, 4.0]))


def display_grade(grade):  
    ''' Break a grade such as "A+" into "A" and "+" '''
    assert len(grade) == 2
    assert type(grade) == str
    assert letter in ["A", "B", "C", "D", "F"]
    
    letter = grade[0]
    sign   = grade[1]
    assert sign in ["+", "-", "", ""]
    assert letter in ["A", "B", "C", "D", "F"]
    
    print("Your letter grade is", letter, "and your sign is", sign)

def compute_tax (income):
    ''' Compute the tax burden based on income. '''
    assert income >= 0
    assert type(income) == float or type(income) == int
    
    tax = None 
    
    # 10% bracket.
    if 0 <= income < 15100:
        tax = income * 0.10
    # 15% bracket.
    elif 15100 <= income < 61300:
        tax = 1510 + 0.15 * (income - 15100)
    # 25% bracket.
    elif 61300 <= income < 123700:
        tax = 8440 + 0.25 * (income - 61300)
    # 28% bracket.
    elif 123700 <= income < 188450:
        tax = 24040 + 0.28 * (income - 123700)
    #33% bracket.
    elif 188450 <= income < 336550:
        tax = 42170 + 0.33 * (income - 188450)
    #35% bracket.
    elif income >= 336550:
        tax = 91043 + 0.35 * (income - 336550)

    assert tax >= 0
    assert type(tax) == float
    assert tax < income
    assert tax != None    
    return tax 

def binary_search(array, search):
    ''' Return TRUE if search exists in array. '''
    assert type(array) == list
    if __debug__:
        for element in array:
            assert type(element) == type(search)
        for i in range(len(array)):
            assert array[i-1] <= array[i]    
    # Initialize the bounding indices.
    i_first = 0
    i_last = len(array) - 1
    assert i_first <= i_last
    assert i_first >= 0
    assert i_last < len(array)
    
    
   # Continue as long as there are elements in the range.
    while i_first <= i_last:
        i_middle = (i_first + i_last) // 2
        assert 0<= i_first <= i_middle <= i_last <= len(array)
       # Too high or too low.
        if array[i_middle] < search:
            i_first = i_middle + 1
        elif array[i_middle] > search:
            i_last = i_middle - 1

        # Found!
        else:
            assert search in array
            return True
    assert len(array) > 0
    
    # Not found!
    assert not search in array
    return False