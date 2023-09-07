def eas503_ex27(month, day):

    # The year is divided into four season: spring, summer, fall (or autumn) and winter.
    # While the exact dates that the seasons change vary a little bit from year to
    # year because of the way that the calender is constructed, we will use the following
    # dates for this exercise:

    # Season  -- First Day
    # Spring  -- March 20
    # Summer  -- June 21
    # Fall  -- September 22
    # Winter    -- December 21

    # Complete this function which takes in as inputs a month and day. It should
    # output the season.
    # input 1: month -- str
    # input 2: day -- int

    # output: month -- str (Spring, Summer, Fall, Winter)

    # BEGIN SOLUTION
    springStart = ('March', 20)
    summerStart = ('June', 21)
    fallStart = ('September', 22)
    winterStart = ('December', 21)

    if month == springStart[0] and day > springStart[1]:
        return 'Spring'
    if month in ('April','May'):
        return 'Spring'
    if month == summerStart[0] and day >= summerStart[1]:
        return 'Summer'
    if month in ('July','August','September'):
        return 'Summer'
    if month == fallStart[0] and day >= fallStart[1]:
        return 'Fall'
    if month in ('October','November'):
        return 'Fall'
    if month == winterStart[0] and day >= winterStart[1]:
        return 'Winter'
    else:
        return 'Winter'
    # END SOLUTION


def eas503_ex28(year):
    # Complete this function to check if year is a leap year
    # Input: year
    # Output: True or False (Boolean)

    # BEGIN SOLUTION
    if (year % 4 == 0):
        if (year % 100) == 0:
            if year % 400 == 0:
                return True
            else: 
               return False
        else:
            return True
    else:
        return False


    # END SOLUTION


def eas503_ex29(month, day, year):
    # Complete this function to check if a data is valid, given month, day, and year.
    # For example, 5/24/1962 is valid, but 9/31/2000 is not
    # Inputs: month, day, year
    # Output: True or False (Boolean)
    # IMPORTANT: Use the function ex28() to determine if year is leap year

    # BEGIN SOLUTION
    if month < 1 or month > 12:
        return False
    daysInMonth = [31, 28 + eas503_ex28(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > daysInMonth[month - 1]:
        return False
    return True
    # END SOLUTION


def eas503_ex30(month, day, year):
    # Complete this function to calculate the day_number given month, day, and year.
    # Information: The days of the year are often numbered from 1 through 365 (or 366).
    # This number can be computed in three steps using int arithmetic:
    # (a) - day_num = 31 * (month - 1) + day
    # (b) - if the month is after February subtract (4*(month)+23)//10
    # (c) - if it's a leap year and after February 29, add 1
    # Hint: First verify the input date is valid, return False if it is not valid; use is_date_valid
    # IMPORTANT: use the functions you wrote previous, namely, ex28 and ex29.
    # Inputs: month, day, year
    # Output: the day number or False (boolean) if the date is invalid.

    # BEGIN SOLUTION
    if not eas503_ex29(month,day,year):
        return False
    day_num = 31*(month - 1) + day
    if eas503_ex28(year) and month > 2:
        day_num = day_num + 1
    if month > 2: 
       day_num -= (4*(month)+23)//10
    return day_num

    # END SOLUTION


def eas503_ex31(plate):

    # In a particular jurisdiction, older license plates consist of three uppercase
    # letters followed by three digits. When all of the license plates following
    # that pattern had been used, the format was changed to four digits followed by
    # three uppercase letters.

    # Complete this function whose only input is a license plate and its output
    # is: 1) Older/Valid 2) Newer/Valid 3) Invalid
    # input: plate (str)
    # output: 'Older/Valid' or 'Newer/Valid' or 'Invalid'
    # HINT: Use the comparator operators (>=, <=)!

    # BEGIN SOLUTION
    if len(plate) == 6:
        if plate[:3].isupper() and plate[3:].isdigit():
            return 'Older/Valid'
    if len(plate) == 7:
        if plate[:4].isdigit() and plate[4:].isupper():
            return 'Newer/Valid'
    return 'Invalid'
    # END SOLUTION


def eas503_ex32(date):

    # A magic date is a date where the day multiplied by the month is equal
    # to the two digit year. For example, June 10, 1960 is a magic date because
    # June is the sixth month, and 6 times 10 is 60, which is equal to the two
    # digit year. Complete this function to determine whether or not a date is
    # a magic date.

    # input: date (str -- month/day/year) -- e.g., 06/01/2022 -- will have leading zero before month and day
    # output: True or False (bool)
    # Hint: use string indexing to extract the month, day, and year from the date string

    # BEGIN SOLUTION
    month,day,year = date.split('/')
    if int(month) * int(day) == int(year[-2:]):
        return True
    return False
    # END SOLUTION

def eas503_ex33(password):
    # In this exercise you will complete this function to determine whether or not
    # a password is good. We will define a good password to be a one that is at least
    # 8 characters long and contains at least one uppercase letter, at least one lowercase
    # letter, at least one number, and at least one of the following special characters (!, @, #, $, ^).
    # This function should return True if the password
    # passed to it as its only parameter is good. Otherwise it should return False.
    #
    # input: password (str)
    # output: True or False (bool)
    # BEGIN SOLUTION

    specialCaseCharacters = '(!, @, #, $, ^)'
    if len(password) >= 8:
        if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in specialCaseCharacters for c in password):
            return True
        
    return False
            
    # END SOLUTION


def eas503_ex34(sentence):
    # Complete this function to calculate the average
    # word length in a sentence
    # Input: sentence
    # Output: average word length in sentence
    # Hint: count punctuations with whatever word they are `touching`
    # Hint: round the average to two decimal places

    # BEGIN SOLUTION
    charCount = len(sentence.replace(" ",""))
    wordCount = len(sentence.split())
    average = round((charCount/wordCount),2)
    return average

    # END SOLUTION


def eas503_ex35(filename):
    # Complete this function to count the number of lines, words, and chars in a file.
    # Input: filename
    # Output: a tuple with line count, word count, and char count -- in this order

    # BEGIN SOLUTION
    lineCount = 0
    wordCount = 0
    charCount = 0
    with open(filename) as file:
      for lines in file:
          lineCount = lineCount + 1
          wordCount = wordCount + len(lines.split())
          charCount = charCount + len(lines)
          
    return (lineCount,wordCount,charCount)

          
          
    
    # END SOLUTION


def eas503_ex36(apr):
    # Complete this function to use a while loop to determine how long it takes for an investment
    # to double at a given interest rate. The input to this function, apr, is the annualized interest rate
    # and the output is the number of years it takes an investment to double. Note: The amount of the initial
    # investment (principal) does not matter; you can use $1.
    # Hint: principal is the amount of money being invested.
    # apr is the annual percentage rate expressed as a decimal number.
    # Relationship: value after one year is given by principal * (1+ apr)

    # BEGIN SOLUTION
    year = 0
    principal = 1
    while principal < 2:
        principal = principal*(1+apr)
        year = year + 1
    return year



    # END SOLUTION


def eas503_ex37(n):
    # Complete this function to return the number of steps taken to reach 1 in
    # the Collatz sequence (https://en.wikipedia.org/wiki/Collatz_conjecture) given n

    # BEGIN SOLUTION
    steps = 0
    while n != 1:
       if (n%2 == 0):
          n = n//2
       else: 
          n = (3*n +1)
       steps = steps + 1
    
    return steps
    
    # END SOLUTION


def eas503_ex38(n):
    # A positive whole number > 2 is prime if no number between 2 and sqrt(n)
    # (include) evenly divides n. Write a program that accepts a value of n as
    # input and determine if the value is prime. If n is not prime, your program should
    # return False (boolean) as soon as it finds a value that evenly divides n.
    # Hint: if number is 2, return False

    import math
    r = 2
    # BEGIN SOLUTION
    if n == 2:
        return False
    if n > 2:
        while r <= int(math.sqrt(n)):
            if(n%r) == 0:
                return False
            r = r + 1
    return True
    # END SOLUTION


def eas503_ex39(n):
    # Complete this function to return all the primes as a list less than or equal to n
    # Input: n
    # Output: a list of numbers
    # hint use ex6

    # BEGIN SOLUTION
    list = []
    num = 2
    while num <= n:
        if eas503_ex38(num):
            list.append(num)
        num = num+1
    
    return list

    # END SOLUTION


def eas503_ex40(m, n):
    # Complete this function to determine the greatest common divisor (GCD).
    # The GCD of two values can be computed using Euclid's algorithm. Starting with the values
    # m and n, we repeatedly apply the formula: n, m = m, n%m until m is 0. At this point, n is the GCD
    # of the original m and n.
    # Inputs: m and n which are both natural numbers
    # Output: gcd

    # BEGIN SOLUTION
    while m != 0:
        n, m = m, n%m
        # temp = n
        # n =  m
        # m = temp%m 
    return n  
    # END SOLUTION


def eas503_ex41(filename):
    # Complete this function to read grades from a file and determine the student with the highest average
    # test grades and the lowest average test grades.
    # Input: filename
    # Output: a tuple containing four elements: name of student with highest average, their average,
    # name of the student with the lowest test grade, and their average. Example ('Student1', 99.50, 'Student5', 65.50)
    # Hint: Round to two decimal places

    # BEGIN SOLUTION
    studentNameList = []
    averageList = []
    with open(filename) as file:
        for line in file:
            sum = 0
            marks = []
            elementList = line.strip().split(',')
            studentNameList.append(elementList[0])
            marks = elementList[1:]
            for mark in marks:
                sum = sum + int(mark)
            average = round(sum/len(marks),2)
            averageList.append(average)
        maxValue = max(averageList)
        maxIndex = averageList.index(maxValue)
        studentMax = studentNameList[maxIndex]
        minValue = min(averageList) 
        minIndex = averageList.index(minValue) 
        studentMin = studentNameList[minIndex]
    return(studentMax,maxValue,studentMin,minValue)   
  
    # END SOLUTION


def eas503_ex42(data, num_outliers):
    # When analyzing data collected as a part of a science experiment it
    # may be desirable to remove the most extreme values before performing
    # other calculations. Complete this function which takes a list of
    # values and an non-negative integer, num_outliers, as its parameters.
    # The function should create a new copy of the list with the num_outliers
    # largest elements and the num_outliers smallest elements removed.
    # Then it should return teh new copy of the list as the function's only
    # result. The order of the elements in the returned list does not have to
    # match the order of the elements in the original list.
    # input1: data (list)
    # input2: num_outliers (int)

    # output: list

    # BEGIN SOLUTION
    sorted_data = sorted(data)
    trimmed_data = sorted_data[num_outliers:len(sorted_data)-num_outliers]
    return trimmed_data
    # END SOLUTION


def eas503_ex43(words):
    # Complete this function to remove duplicates from the words list using a loop
    # input: words (list)
    # output: a list without duplicates
    # MUST USE loop and NOT set!
    # Preserve order

    # BEGIN SOLUTION
    uniqueWordList = []
    for word in words:
        if word not in uniqueWordList:
            uniqueWordList.append(word)
    return uniqueWordList
           

    # END SOLUTION


def eas503_ex44(n):
    # A proper divisor ofa  positive integer, n, is a positive integer less than n which divides
    # evenly into n. Complete this function to compute all the proper divisors of a positive
    # integer. The integer is passed to this function as the only parameter. The function will
    # return a list of containing all of the proper divisors as its only result.

    # input: n (int)
    # output: list

    # BEGIN SOLUTION
    divisorList = []
    for num in range(1,n):
        if n%num == 0:
            divisorList.append(num)
    return divisorList
    # END SOLUTION


def eas503_ex45(n):
    # An integer, n, is said to be perfect when the sum of all of the proper divisors
    # of n is equal to n. For example, 28 is a perfect number because its proper divisors
    # are 1, 2, 4, 7, and 14 = 28
    # Complete this function to determine if a the number a perfect number or not.
    # input: n (int)
    # output: True or False (bool)

    # BEGIN SOLUTION
    sum = 0
    for num in range(1,n):
        if n%num == 0:
            sum = sum + num
    if sum == n:
        return True
    return False

    # END SOLUTION


def eas503_ex46(points):
    # Complete this function to determine the best line.
    # https://www.varsitytutors.com/hotmath/hotmath_help/topics/line-of-best-fit
    # input: points (list of tuples contain x, y values)
    # output: (m, b) # round both values to two decimal places

    # BEGIN SOLUTION
    xtotal = 0 
    ytotal = 0
    for point in points:
        xtotal = xtotal + point[0]
        ytotal = ytotal + point[1]
    xmean = xtotal/len(points)
    ymean = ytotal/len(points)
    numerator = 0
    denominator = 0
    for point in points:
        numerator +=  ((point[0]-xmean)*(point[1]-ymean))
        denominator += ((point[0]-xmean)*(point[0]-xmean))
    m = round(numerator / denominator, 2)
    b = round(ymean - (numerator / denominator)*xmean,2)
    return (m,b)  



    # END SOLUTION


def eas503_ex47(title, header, data, filename):
    # This problem is hard.
    # Open up ex15_*_solution.txt and look at the output based on the input parameters, which
    # can be found in the test_assignment4.py file
    # Function inputs: 
    # title -- title of the table -- a string
    # header -- header of the table  -- a tuple
    # data -- rows of data, which is a tuple of tuples
    # filename -- name of file to write the table to
    # Your job is to create the table in the file and write it to `filename`
    # Note that you need to dynamically figure out the width of each column based on 
    # maximum possible length based on the header and data. This is what makes this problem hard. 
    # Once you have determined the maximum length of each column, make sure to pad it with 1 space
    # to the right and left. Center align all the values. 
    # OUTPUT: you are writing the table to a file

    # BEGIN SOLUTION
    title = '|' + '{:^51}'.format({title}) + '|'
    line = '+' + '-'*15 + '+' + ('-'*8 + '+')*4
    row = '| {:<13} |' + ' {:6,d} |'*4
    header = '| {:^13s} |'.format({header.split(,)}) + (' {:^6d} |'*4).format(1980, 1990,
                                                                  2000, 2010)
    print('+' + '-'*(len(title)-2) + '+',
         title,
         line,
         header,
         line,
         row.format('China', 2937, 4321, 4752, 5527),
         row.format('Germany', 4225, 5411, 6453, 6718),
         row.format('United States', 3772, 4755, 5854, 6988),
         line,
         sep='\n')

    # END SOLUTION

def eas503_ex48(filename):
    """
    In this problem you will read data from a file and perform a simple mathematical operation on each data point. 
    Each line is supposed to contain a floating point number.
    But what you will observe is that some lines might have erroneous entries. 
    You need to ignore those lines (Hint: Use Exception handling).

    The idea is to implement a function which reads in a file and computes the median 
    of the numbers and returns the output. You may use the inbuilt function sort when computing the median.

    DO NOT USE ANY INBUILT OR OTHER FUNCTION TO DIRECTLY COMPUTE MEDIAN

    """
    ### BEGIN SOLUTION
    list = []
    with open(filename) as file:
        for line in file:
            value = line.strip()
            try:
                list.append(float(value))
            except:
                print("error")

        sortedList = sorted(list)
        if len(list) > 0:
             if len(list) % 2 == 0:
                 median = (sortedList[int((len(list)/2)-1)] + sortedList[int((len(list)/2))])/2
             else:
                 median = sortedList[int((len(list)/2))]
        else:
            return "The file does not have any valid number to compute the median"
    return median


            



  
    ### END SOLUTION