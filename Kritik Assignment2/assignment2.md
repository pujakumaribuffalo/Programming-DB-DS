# Assignment 2

Kaeleigh has emailed you a CSV file with four columns: UBID, enrollment date, graduation date, and student type (either Full-Time or Part-Time). She has requested that you develop a program to filter the file in order to identify students who meet specific criteria. Specifically, you need to identify full-time students who took more than four years to graduate and part-time students who took more than seven years to graduate. The resulting CSV file should only include the students who meet these criteria. It should have the same columns as the original file, including the header row, and an additional column called "NumberOfYears." 


## Guideline
**PLEASE READ CAREFULLY!!!**
1. Filter `input.csv` to create a new file called `output.csv`
2. Just take the difference between the year and do not worry about months. 
3. Submit the complete code and answer to each question as an HTML file converted from markdown. Just modify the attached markdown file.
4. When grading, run the code to verify the output and then grade the answers to each question to assess if they make sense. 


## Working Code

```python

# Open the input file for reading
def filter_students(input_file, output_file):
    input_file = 'input.csv'
    output_file = 'output.csv'
    with open(input_file, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        header.append('NumberOfYears')

        filtered_rows = [header]

        for line in lines[1:]:
            row = line.strip().split(',')
            if not any(row):
                continue

            ubid = row[0]
            enrollment_date = row[1]
            graduation_date = row[2]
            student_type = row[3]

            enrollment_year = int(enrollment_date[-4:])
            graduation_year = int(graduation_date[-4:])
            number_of_years = graduation_year - enrollment_year

            if (student_type == 'Full-Time' and number_of_years > 4) or (student_type == 'Part-Time' and number_of_years > 7):
                row.append(str(number_of_years))
                filtered_rows.append(row)

    with open(output_file, 'w') as output_file:
        for row in filtered_rows:
            output_file.write(','.join(row) + '\n')


```


## Questions
For each question, reference the actual code and provide a brief explanation. 


1. How do you open a file for reading?
   ```python
   with open('input.csv', 'r') as file:
   ```
   To open a file for reading, you can use the open() function with the file path and the mode 'r'. The with statement is used to ensure proper handling of file resources. The file is opened as file, and you can read its contents using methods like readlines()

2. How do you handle the difference between a CSV and TSV file?
    
    In the given code, there is no specific handling for distinguishing between a CSV (comma-separated values) file and a TSV (tab-separated values) file. It assumes that the file is comma-separated. If you have a TSV file, where values are separated by tabs, you would need to modify the code accordingly. For example, you can split the lines using line.split('\t') to handle TSV files.

3. How do you skip empty lines?
   ```python
   if not any(row):
    continue
   ```
   To skip empty lines, we can check if any value exists in the current row using the any() function. If there are no values (i.e., the row is empty), the continue statement is used to move to the next iteration, skipping the empty line.

4. How do you read one line at a time instead of reading the whole line at once?
   
   The code reads one line at a time by using a for loop. By iterating over the lines list starting from the second line (lines[1:]), each line is assigned to the line variable. Then, the line is stripped of leading/trailing whitespace using strip() and split into a list of values using split(',').
   ```python
   for line in lines[1:]:
       row = line.strip().split(',')
   ```
   
5. How do you update the header to include an an additional column?
   ```python
   header = lines[0].strip().split(',')
   header.append('NumberOfYears')
   ```
   The header is extracted from the first line of the file (lines[0]). It is stripped of leading/trailing whitespace using strip() and split into a list of column names using split(','). Then, the additional column name, 'NumberOfYears', is appended to the header list using append().

6. How do you apply the criteria specified in the question?
   ```python
   if (student_type == 'Full-Time' and number_of_years > 4) or (student_type == 'Part-Time' and number_of_years > 7):
      filtered_rows.append(row)
    # Code inside the if statement to handle the row meeting the criteria
   ```
   The code applies the criteria specified in the question using an if statement. It checks if the student type is "Full-Time" and the number of years is greater than 4, or if the student type is "Part-Time" and the number of years is greater than 7. If the criteria are met, the row list is appended to the filtered_rows lis.

7. How do you open a file for writing?
   ```python
   with open('output.csv', 'w', newline='') as output_file:
    # Code inside the block to write to the file
   ```
   To open a file for writing, we can use the open() function with the file path and the mode 'w'. The with statement is used to ensure proper handling of file resources. The file is opened as output_file, and we can perform the desired writing operations inside the block.

8.  How do you save the header to use for later?
    ```python
    header = lines[0].strip().split(',')
    filtered_rows = [header]
    ```
    
    The header is saved for later use by storing it in the header list. This list is initialized with the header row read from the input file. Later, when writing the filtered rows to the output file, the header is written first before writing the rows.

    
9.  How do you write the lines/rows that meet the criteria? 
    ```python
    with open(output_file, 'w') as output_file:
    for row in filtered_rows:
        output_file.write(','.join(row) + '\n')
    ```
    
    After filtering the rows, the code iterates over the filtered_rows list and writes each row to the output file using the write() method. The row values are joined into a string using ','.join(row), and a newline character is added at the end of each line.By repeating this process for each row in the filtered_rows list, the code writes all the lines/rows that meet the criteria to the output file, with each row separated by a newline character.

10. How do you handle the fact that some columns are string and others are ints when writing the lines/rows?
    ```python
    if (student_type == 'Full-Time' and number_of_years > 4) or (student_type == 'Part-Time' and number_of_years > 7):
        row.append(str(number_of_years))
        filtered_rows.append(row)
    ```
    
    The code assumes that all values are strings, including the additional column "NumberOfYears". It converts the number_of_years to a string using str(number_of_years) before appending it to the row list. The row values are then joined into a string using ','.join(row) before writing to the file. If we want to enforce specific data types for certain columns, we would need to perform explicit type conversions before appending the values to the row list.
  

