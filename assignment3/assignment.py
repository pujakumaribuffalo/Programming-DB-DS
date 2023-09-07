def eas503_ex49(filename):
    # Complete this function to read grades from `filename` and find the minimum
    # student test averages. File has student_name, test1_score, test2_score,
    # test3_score, test4_score, test5_score. This function must use a lambda
    # function and use the min() function to find the student with the minimum
    # test average. The input to the min function should be
    # a list of lines. Ex. ['student1,33,34,35,36,45', 'student2,33,34,35,36,75']
    # input filename
    # output: (lambda_func, line_with_min_student) -- example (lambda_func, 'student1,33,34,35,36,45')

    # BEGIN SOLUTION
    # Read lines from the input file
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    lambda_func = lambda line: sum(map(int, line.split(',')[1:])) / 5
    line_with_min_student = min(lines, key=lambda_func)
    return (lambda_func, line_with_min_student)
    # END SOLUTION


def eas503_ex50(filename):
    # Complete this function to read grades from `filename` and map the test average to letter
    # grades using map and lambda. File has student_name, test1_score, test2_score,
    # test3_score, test4_score, test5_score. This function must use a lambda
    # function and map() function.
    # The input to the map function should be
    # a list of lines. Ex. ['student1,73,74,75,76,75', ...]. Output is a list of strings in the format
    # studentname: Letter Grade -- 'student1: C'
    # input filename
    # output: (lambda_func, list_of_studentname_and_lettergrade) -- example (lambda_func, ['student1: C', ...])

    # Use this average to do the grade mapping. Round the average grade.
    # D = 65<=average<70
    # C = 70<=average<80
    # B = 80<=average<90
    # A = 90<=average
    # Define a function that takes in a number grade and returns the letter grade and use
    # it inside the lambda function.
    # HINT: create a function
    
    # BEGIN SOLUTION
    # Define a function to map a number grade to a letter grade

    def num_to_letter_grade(num_grade):
        if num_grade >= 90:
            return 'A'
        elif num_grade >= 80:
            return 'B'
        elif num_grade >= 70:
            return 'C'
        elif num_grade >= 65:
            return 'D'
        else:
            return 'F'
    
    lines = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            lines.append(line)
    

    lambda_func = lambda line: f"{line.split(',')[0]}: {num_to_letter_grade(round(sum(map(int, line.split(',')[1:])) / len(list(map(int, line.split(',')[1:])))))}"
    studentname_and_lettergrade = list(map(lambda_func, lines))
    
    return lambda_func, studentname_and_lettergrade

# END SOLUTION



def eas503_ex51(filename):
    # Complete this function to sort a list of dictionary by 'test3'
    # return the lambda function and the sorted list of dictionaries
    # Use the following code to read JSON file
    import json
    with open(filename) as infile:
         grades = json.load(infile)


    lambda_func = lambda d: int(d['test3'])
    sorted_list = sorted(grades, key=lambda_func)
    return (lambda_func, sorted_list)

    # END SOLUTION


def eas503_ex52(lst):
    # Complete this function to use list comprehension to return all values from `lst`
    # that are a multiple of 3 or 4. Just complete the list comprehension below.
    # input: `lst` of numbers
    # output: a list of numbers

    # BEGIN SOLUTION
    # complete the following line!
    return [x for x in lst if x % 3 == 0 or x % 4 == 0]
    # END SOLUTION


def eas503_ex53(lst):
    # Complete this function to use list comprehension to multiple all numbers
    # in the list by 3 if it is even or 5 if its odd
    # input: `lst` of numbers
    # output: a list of numbers

    # BEGIN SOLUTION
    # complete the following line!
    return [num*3 if num % 2 == 0 else num*5 for num in lst]

    # END SOLUTION


def eas503_ex54(input_dict, test_value):
    # Complete this function to find all the keys in a dictionary that map to the input value.
    # input1: input_dict (dict)
    # input2: test_value
    # output: list of keys

    # BEGIN SOLUTION
    return [key for key, value in input_dict.items() if value == test_value]
    # END SOLUTION
