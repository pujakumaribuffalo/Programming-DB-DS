def eas503_ex1(name):
    # Complete this function to use the `name` input parameter/argument to create the following string and return it:
    # Hello, <name>, nice to meet you!
    # Example: name = Brian
    # Output: "Hello, Brian, nice to meet you!"
    # You must use f-string!!!

    # BEGIN SOLUTION
    return f"Hello, {name}, nice to meet you!"
    # END SOLUTION


def eas503_ex2(x, y, z):
    # Complete this function to use the inputs x, y, and z to return the quoted string.
    # You must use f-string to create each line, but you can use the + operator to join each line
    # or use the new line character inside the f-string to add new lines. 
    """
    The value of x is: <x>.
    The value of y is: <y>.
    The value of z is: <z>.
    """

    # BEGIN SOLUTION
    return f'The value of x is: {x}.\n' + f'The value of y is: {y}.\n' + f'The value of z is: {z}.'
    # END SOLUTION


def eas503_ex3(length, width):
    # Complete this function to use the inputs length and width to
    # calculate the area of a rectangle and return the following string:
    # "The area of a rectangle with length <length> and width <width> is <area>."
    # Make sure to round the area to two decimal places.

    # BEGIN SOLUTION
    area = length * width
    area = round(area,2)
    return f'The area of a rectangle with length {length} and width {width} is {area}.'
    # END SOLUTION


def eas503_ex4(radius):
    # Complete this function to return the surface area of a sphere given a radius.
    # Use the input `radius` as the radius
    # round the surface area to two decimals
    # Use the PI from the math module

    import math
    PI = math.pi
    

    # BEGIN SOLUTION
    surfaceArea = 4*PI*radius*radius
    return round(surfaceArea, 2)
    # END SOLUTION


def eas503_ex5(radius):
    # Complete this function to return the volume of a sphere given a radius.
    # Use the input `radius` as the radius
    # round the volume to two decimals
    # Use the PI from the math module

    import math
    PI = math.pi

    # BEGIN SOLUTION
    volume = (4 * PI * pow(radius, 3))/3
    return round(volume, 2)
    # END SOLUTION


def eas503_ex6(weight, height):
    # The body mass index (BMI) is calculated as a peron's weight (in pounds) times 703, divided by the square
    # of the person's height (in inches). A BMI in the range 19-25, inclusive, is considered healthy.
    # Complete this function to calculate and return a person's BMI
    # Round the BMI to two decimals places using the round function

    # BEGIN SOLUTION
    BMI = (weight*703)/(height*height)
    return round(BMI, 2)
    # END SOLUTION


def eas503_ex7(no_one_liter_bottles, no_more_than_one_liter_bottles):
    # When you buy soda bottles, you deposit a small amount to encourage recycling.
    # For one liter bottle the deposit is $0.10.
    # For a bottle larger than one liter, the deposit is $0.25.
    # Complete this function to print a refund message like follows:
    # The refund amount is $<amount>.
    # Round the refund to two decimal places using f-string format specifier

    # BEGIN SOLUTION
    amount = no_one_liter_bottles* 0.10 + no_more_than_one_liter_bottles* 0.25
    return "The refund amount is $%s." % f'{amount:.2f}'
    # END SOLUTION


def eas503_ex8(a, b):
    # Complete this function to return the following string given two numbers a and b
    """
    The sum of <a> and <b> is <result>.
    The difference when <b> is subtracted from <a> is <result>.
    The product of <a> and <b> is <result>.
    The quotient when <a> is divided by <b> is <result>.
    The remainder when <a> is divided by <b> is <result>. 
    The result of <a>^<b> is <result>. 
    """

    # Return just one string that has multiple lines. use f-string and + to concatenate lines

    # BEGIN SOLUTION
    return f'The sum of {a} and {b} is {a+b}.\n' + f'The difference when {b} is subtracted from {a} is {a-b}.\n'+f'The product of {a} and {b} is {a*b}.\n'+ f'The quotient when {a} is divided by {b} is {a//b}.\n'+ f'The remainder when {a} is divided by {b} is {a%b}.\n'+ f'The result of {a}^{b} is {pow(a,b)}.' 
   
    # END SOLUTION


def eas503_ex9(P, r, t):
    # The formula for simple interest is A = P(1+rt), where P is
    # the principle amount, r is the annual rate of interest,
    # t is the number of years the amount is invested, and A
    # is the amount at the end of the investment.
    # Complete this function to return the following string:
    # After <t> years at <r>%, the investment will be worth $<A>.
    # Round the amount to two decimal places using f-string
    # Hint: rate is a percentage!

    # BEGIN SOLUTION
    A = P + P*r*t/100
    return f'After {t} years at {r}%, the investment will be worth ${A:.2f}.'
    # END SOLUTION


def eas503_ex10(P, r, t, n):
    # The formula for compound interest is
    # A = P(1 + r/n)^nt
    # where:
    # P is the principle amount.
    # r is the annual rate of interest.
    # t is the number of years the amount is invested.
    # n is the number of times the interest is compounded per year.
    # A is the amount at the end of the investment.
    # Complete this function to return the following string:
    # $<P> invested at <r>% for <t> years compounded <n> times per year is $<A>.
    # round to two decimal places using f-string formatting

    # BEGIN SOLUTION
    A = P*(pow((1+ r/(100*n)),(n*t)))
    return f'${P} invested at {r}% for {t} years compounded {n} times per year is ${A:.2f}.'
    # END SOLUTION


def eas503_ex11(input_string):
    """
    This function takes in one input string. Complete this function to return
    the input string and the number of characters in the input string.
    Sample Input: Amherst
    Expected return string: The input string 'Amherst' has 7 characters. 
    - Use f-string
    """

    # BEGIN SOLUTION
    return f"The input string '{input_string}' has {len(input_string)} characters."
    # END SOLUTION


def eas503_ex12(noun, verb, adjective, adverb):
    """
    This function takes in four input strings. Complete this function to return
    a sentence using the four input strings
    Input Strings: noun, verb, adjective, adverb
    Expected print Statement: Do you <verb> your <adjective> <noun> <adverb>? That's hilarious!
    - Use f-string
    """

    # BEGIN SOLUTION
    return f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"
    # END SOLUTION


def eas503_ex13(current_age, age_at_retirement, current_year):
    """
    This function takes in three numbers as input arguments: current_age, age_at_retirement, and current_year. 
    Complete this function to return the expected output string. 

    If current_age = 36, age_at_retirement = 72, and current_year = 2021

    Expected output:
    Your current age is: 36.
    You would like to retire at: 72.
    You have 36 years left until you can retire.
    It's 2021, so you can retire in 2057.

    - Use f-string
    """

    # BEGIN SOLUTION
    
    return f'Your current age is: {current_age}.\n' +  f'You would like to retire at: {age_at_retirement}.\n' + f'You have {age_at_retirement - current_age} years left until you can retire.\n'+ f"It's {current_year}, so you can retire in {current_year+(age_at_retirement - current_age)}."
   
    
    # END SOLUTION


def eas503_ex14(length, width):
    """
    This function takes in the length and width in feet. 
    Complete this function to return the expected output string. 
    Use formula -- m^2 = f^2 * 0.09290304 to convert feet^2 to meter^2

    If length = 15 and width = 20

    Expected output:
    The length of the room in feet is 15.
    The width of the room in feet is 20.
    The dimension of the room is 15 by 20 feet.
    The area is
    300 square feet
    27.87 square meters

    - Use f-string
    """

    # BEGIN SOLUTION

    
    return f'The length of the room in feet is {length}.\n'+ f'The width of the room in feet is {width}.\n'+ f'The dimension of the room is {length} by {width} feet.\n'+ f'The area is\n' + f'{length*width} square feet\n'+ f'{(length*width*0.09290304):.2f} square meters'
    # END SOLUTION


def eas503_ex15(number_of_people, number_of_pizzas):
    """
    This function takes in the number of people and the number of pizzas. Assume each pizza has 8 slices. 

    Complete this function to return the expected output string. 

    If number_of_people = 8 and number_of_pizzas = 2

    Expected output:
    There are 8 people with 2 pizzas.
    Each person gets 2 pieces of pizza.
    There are 0 leftover pieces.

    - Use f-string
    """

    # BEGIN SOLUTION
    return f"There are {number_of_people} people with {number_of_pizzas} pizzas.\n" + f'Each person gets {(number_of_pizzas*8)// number_of_people} pieces of pizza.\n'+ f"There are {(number_of_pizzas*8)%number_of_people} leftover pieces."
    # END SOLUTION


def eas503_ex16(length, width):
    """
    This function takes in the length and width in feet of a ceiling. You need to calculate the number
    of gallons needed to paint the ceiling. Assuming one gallon can paint 350 square feet. 

    Complete this function to return the expected output string. 

    If length = 12 and width = 30

    Expected output:
    You will need to purchase 2 gallons of paint to cover 360 square feet.

    - Use f-string
    - HINT: You need to use the math.ceil function to round up
    """

    import math
    # BEGIN SOLUTION
    return f"You will need to purchase {math.ceil((length*width)/350)} gallons of paint to cover {length * width} square feet."
    # END SOLUTION


def eas503_ex17(value):
    """
    You must use f-string formatting to get the output string: "The value is: 3.1416." This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output. Do not use the round
    function. Rather, use f-string for rounding. Make sure to return the output string!
    """

    # BEGIN SOLUTION
    return f"The value is:{value: .4f}."
    # END SOLUTION


def eas503_ex18(value):
    """
    You must use f-string formatting to get the following string output: "The value is:     3.1416." This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output. Do not just put
    spaces inside the f-string. Use f-string format specifiers to adjust justification and width. 
    """

    # BEGIN SOLUTION
    return f"The value is:{value: 11.4f}."
    # END SOLUTION


def eas503_ex19(value):
    """
    You must use f-string formatting to get the following string output: "The value is: 3.141590--.". This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output. 
    """

    # BEGIN SOLUTION
    return f"The value is: {value:.6f}--."
    # END SOLUTION


def eas503_ex20(value):
    """
    You must use f-string formatting to get the following output string: "The value is: --3.141590--." This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output.   
    """
    # BEGIN SOLUTION
    return f"The value is: --{value:.6f}--."
    # END SOLUTION

def eas503_ex21(hours, wage):
    # Many companies pay time-and-a-half for any hours worked above 40 in a given week.
    # Complete this function whose inputs are hours worked (hours) and the hourly rate (wage) to
    # calculate the total wages for the week.
    #
    # BEGIN SOLUTION
    
    
    if hours > 40:
       totalWage =  wage*40 + 1.5*wage*(hours-40)
    else:
        totalWage = wage*hours
    return totalWage
    # END SOLUTION


def eas503_ex22(score):
    # A certain CS professor gives five-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F.
    # Complete this function which accepts a quiz score as an input and uses a decision structure to calculate the corresponding
    # grade.
    # BEGIN SOLUTION
    if score == 5:
        return'A'
    elif score == 4:
        return 'B'
    elif score == 3:
        return 'C'
    elif score == 2:
        return 'D'
    else:
        return 'F'
    # END SOLUTION


def eas503_ex23(score):
    # A certain CS professor gives 100-point exams that are graded on the scale 90-100: A, 80-89: B, 70-79: C,
    # 60-69: D, < 60: F. Complete this function which accepts an exam score as input and uses a decision structure
    # to calculate the corresponding grade.
    # BEGIN SOLUTION
    if score in range(90,100):
        return'A'
    elif score in range(80,89):
        return 'B'
    elif score in range(70,79):
        return 'C'
    elif score in range(60,69):
        return 'D'
    else:
        return 'F'
    # END SOLUTION


def eas503_ex24(credits):
    # A certain college classifies students according to credits earned. A student with less than 7 credits is a Freshman.
    # At least 7 credits are required to be a Sophomore, 16 to be a Junior and 26 to be classified as Senior.
    # Complete this function which calculates the class standing from the number of credits earned.
    # BEGIN SOLUTION
    if credits < 7:
        return 'Freshman'
    elif credits >= 7 and credits < 16:
        return 'Sophomore'
    elif credits >= 16 and credits < 26:
        return 'Junior'
    elif credits >= 26:
        return 'Senior'
    # END SOLUTION


def eas503_ex25(limit, speed):
    # The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the limit plus a
    # penalty of $200 for any speed over 90 mph. Complete this function which accepts a speed limit and a clocked
    # speed and either return the string `Legal` or the amount of fine, if the speed is illegal.
    # BEGIN SOLUTION
    if speed <= limit:
        return "Legal"
    elif speed > limit and speed <= 90:
        amount = 50 + (speed-limit)*5
        return amount
    else:
        amount = 50 + (speed-limit)*5 + 200
        return amount
    
    # END SOLUTION


def eas503_ex26(input_string):
    # Complete this function to determine if the input_string is a palindrome. Return True or False
    # Use square brackets to reverse the input_string! Make sure to lower the input string before testing!
    # BEGIN SOLUTION
    input_string = input_string.lower()
    reversedString = input_string[::-1]
    if input_string == reversedString:
        return True
    return False
    # END SOLUTION
