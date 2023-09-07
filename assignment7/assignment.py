import sqlite3
from sqlite3 import Error
import numpy as np
import pandas as pd
from faker import Faker


pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)

def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except sqlite3.Error as e:
        print(e)

    return conn


conn = create_connection('non_normalized.db')
sql_statement = "select * from Students;"
df = pd.read_sql_query(sql_statement, conn)
# print(df)

def create_df_degrees(non_normalized_db_filename):
    """
    Open connection to the non-normalized database and generate a 'df_degrees' dataframe that contains only
    the degrees. See screenshot below. 
    """

    # BEGIN SOLUTION
    conn = create_connection(non_normalized_db_filename)
    
    # Execute SQL query to fetch the degrees
    df_degrees = pd.DataFrame({'Degree': df['Degree'].unique()})
    
    # Close the database connection
    conn.close()
    
    return df_degrees
    # END SOLUTION


def create_df_exams(non_normalized_db_filename):
    """
    Open connection to the non-normalized database and generate a 'df_exams' dataframe that contains only
    the exams. See screenshot below. Sort by exam!
    hints:
    # https://stackoverflow.com/a/16476974
    # https://stackoverflow.com/a/36108422
    """

    # BEGIN SOLUTION

    df_exams = df['Exams'].str.extractall(r'(exam\d+)\s\((\d+)\)').reset_index(drop=True)
    df_exams.columns = ['Exam', 'Year']

    df_exams = df_exams.sort_values('Exam')
    df_exams_unique = df_exams.drop_duplicates()
    df_exams_unique.reset_index(drop=True, inplace=True)
    df_exams_unique = df_exams_unique.copy()

    # Convert 'Year' column to int64
    df_exams_unique['Year'] = df_exams_unique['Year'].astype('int64')   
    return df_exams_unique
    # END SOLUTION

  


def create_df_students(non_normalized_db_filename):
    """
    Open connection to the non-normalized database and generate a 'df_students' dataframe that contains the student
    first name, last name, and degree. You will need to add another StudentID column to do pandas merge.
    See screenshot below. 
    You can use the original StudentID from the table. 
    hint: use .split on the column name!
    """

    # BEGIN SOLUTION
    df_students = df

    # Splitting the Name column into First_Name and Last_Name
    df_students[['Last_Name', 'First_Name']] = df_students['Name'].str.split(', ', expand=True)

    # Reordering the columns
    df_students = df_students[['StudentID', 'First_Name', 'Last_Name', 'Degree']]

    return df_students
    # END SOLUTION
    


def create_df_studentexamscores(non_normalized_db_filename, df_students):
    """
    Open connection to the non-normalized database and generate a 'df_studentexamscores' dataframe that 
    contains StudentID, exam and score
    See screenshot below. 
    """

    # BEGIN SOLUTION
    merged_df = pd.merge(df, df_students, on='StudentID')  
     
    # Split Exams and Scores into separate rows
    exams = merged_df['Exams'].str.split(', ')
    scores = merged_df['Scores'].str.split(', ')

    # Remove the year from the exam names
    exams = exams.apply(lambda x: [exam.split()[0] for exam in x])

    df_output = pd.DataFrame({
        'StudentID': merged_df['StudentID'].repeat(exams.str.len()),
        'Exam': [exam for sublist in exams for exam in sublist],
        'Score': [score for sublist in scores for score in sublist]
    })

    # Reset the index
    df_output = df_output.reset_index(drop=True)

    # Convert 'Score' column to int64
    df_output['Score'] = df_output['Score'].astype('int64') 
    return  df_output                  
        
    # END SOLUTION


def ex1(df_exams):
    """
    return df_exams sorted by year
    """
    # BEGIN SOLUTION
    df_exams = df_exams.sort_values('Year')
    # END SOLUTION
    return df_exams


def ex2(df_students):
    """
    return a df frame with the degree count
    # NOTE -- rename name the degree column to Count!!!
    """
    if 'Degree' not in df_students.columns:
        raise ValueError("Column 'Degree' not found in df_students DataFrame.")

    output = pd.DataFrame({'Count': df['Degree'].value_counts()})
    return output
    #END SOLUTION
   


def ex3(df_studentexamscores, df_exams):
    """
    return a datafram that merges df_studentexamscores and df_exams and finds the average of the exams. Sort
    the average in descending order. See screenshot below of the output. You have to fix up the column/index names.
    Hints:
    # https://stackoverflow.com/a/45451905
    # https://stackoverflow.com/a/11346337
    # round to two decimal places
    """

    # BEGIN SOLUTION
    # Merge the two dataframes.
    merged_df = pd.merge(df_studentexamscores, df_exams, on='Exam')
    # groups the DataFrame merged_df by the 'Exam' column and selects the 'Year' and 'Score' columns. Then 
    output = merged_df.groupby('Exam')[['Year', 'Score']].mean().rename(columns={'Score': 'average'})
    output = output.round(2).sort_values(by='average', ascending=False)
    return output
    # END SOLUTION


def ex4(df_studentexamscores, df_students):
    """
    return a datafram that merges df_studentexamscores and df_exams and finds the average of the degrees. Sort
    the average in descending order. See screenshot below of the output. You have to fix up the column/index names.
    Hints:
    # https://stackoverflow.com/a/45451905
    # https://stackoverflow.com/a/11346337
    # round to two decimal places
    """

    # BEGIN SOLUTION
    #print("df_students: \n", df_students)
    # Merge df_studentexamscores and df_students on StudentID
    merged_df = pd.merge(df_studentexamscores, df_students, on='StudentID')

    # Calculate average score for each degree
    output = merged_df.groupby('Degree')['Score'].mean().reset_index().rename(columns={'Score': 'Average'})

    # Sort the output DataFrame by Average in descending order
    output = output.sort_values(by='Average', ascending=False)

    # Set 'Degree' column as index
    output = output.set_index('Degree')

    # Round the Average values to two decimal places
    output['Average'] = output['Average'].round(2)

    return output

    # END SOLUTION


def ex5(df_studentexamscores, df_students):
    """
    merge df_studentexamscores and df_students to produce the output below. The output shows the average of the top 
    10 students in descending order. 
    Hint: https://stackoverflow.com/a/20491748
    round to two decimal places

    """
    
    # BEGIN SOLUTION
    merged_df = pd.merge(df_studentexamscores, df_students, on='StudentID')

    # Calculate average score for each student
    average_scores = merged_df.groupby(['First_Name', 'Last_Name', 'Degree'])['Score'].mean().reset_index()

    # Sort the average_scores DataFrame by average in descending order and FirstName as Ascending order.
    sorted_scores = average_scores.sort_values(by=['Score', 'First_Name'], ascending=[False, True])

    # Get the top 10 students
    top_10_students = sorted_scores.head(10)

    # # Remove the 'StudentID' column
    # top_10_students = top_10_students.drop('StudentID', axis=1)

    # Reset the index
    top_10_students = top_10_students.reset_index(drop=True)

    # Rename the 'Score' column to 'average'
    top_10_students = top_10_students.rename(columns={'Score': 'average'})

    # Round the Average values to two decimal places
    top_10_students['average'] = top_10_students['average'].round(2)

    #print("top_10_students : \n", top_10_students)
    return top_10_students
    # END SOLUTION


# DO NOT MODIFY THIS CELL OR THE SEED

# THIS CELL IMPORTS ALL THE LIBRARIES YOU NEED!!!


np.random.seed(0)
fake = Faker()
Faker.seed(0)


def part2_step1():

    # ---- DO NOT CHANGE
    np.random.seed(0)
    fake = Faker()
    Faker.seed(0)
    # ---- DO NOT CHANGE

    # BEGIN SOLUTION

    # Generate a list of 100 usernames, first names, and last names
    num_users = 100
    students = [fake.name() for _ in range(num_users)]
    # Split each student's name into first and last name
    first_names = [name.split(' ', 1)[0] for name in students]
    last_names = [name.split(' ', 1)[1] for name in students]

    # Generate usernames for each student
    usernames = [f"{first_name[:2].lower()}{np.random.randint(1000, 9999)}" for first_name in first_names]

    # Create a DataFrame with the generated data
    data = {
        'Username': usernames,
        'First Name': first_names,
        'Last Name': last_names
    }
    df = pd.DataFrame(data)
    #print(df)
    return df
    # END SOLUTION
    


def part2_step2():

    # ---- DO NOT CHANGE
    np.random.seed(0)
    # ---- DO NOT CHANGE

    # BEGIN SOLUTION
    # Define the data for homework and exams
    data = {
        'Name': ['Hw1', 'Hw2', 'Hw3', 'Hw4', 'Hw5', 'Exam1', 'Exam2', 'Exam3', 'Exam4'],
        'mu': [35, 75, 25, 45, 45, 75, 25, 45, 35],
        'sigma': [9, 15, 7, 10, 5, 20, 8, 9, 10],
        'max score': [50, 100, 40, 60, 50, 100, 50, 60, 50]
    }

    # Create a DataFrame from the data
    df_data = pd.DataFrame(data)

    # Generate the scores for each homework and exam for 100 students
    scores = np.round(np.clip(np.random.normal(df_data['mu'], df_data['sigma'], size=(100, len(df_data))), 0, df_data['max score']))

    # Create a DataFrame with the scores
    df_scores = pd.DataFrame(scores, columns=df_data['Name'])

    # Print the scores DataFrame
    print(df_scores)
    return df_scores
    # END SOLUTION


def part2_step3(df2_scores):
    # BEGIN SOLUTION
    data = {
        'Name': ['Hw1', 'Hw2', 'Hw3', 'Hw4', 'Hw5', 'Exam1', 'Exam2', 'Exam3', 'Exam4'],
        'mu': [35, 75, 25, 45, 45, 75, 25, 45, 35],
        'sigma': [9, 15, 7, 10, 5, 20, 8, 9, 10],
        'max score': [50, 100, 40, 60, 50, 100, 50, 60, 50]
    }

    # Create a DataFrame from the data
    df_data = pd.DataFrame(data)

    # Calculate the mean and standard deviation from describe()
    df_describe = df2_scores.describe().round(2)

    # Calculate the theoretical mean and standard deviation
    mean_theoretical = df_data['mu'].values
    std_theoretical = df_data['sigma'].values

    # Calculate the absolute differences between the describe() and theoretical values
    abs_mean_diff = np.abs(df_describe.loc['mean'] - mean_theoretical).round(2)
    abs_std_diff = np.abs(df_describe.loc['std'] - std_theoretical).round(2)

    # Create a DataFrame with the comparison results
    df_comparison = pd.DataFrame({
        'mean': df_describe.loc['mean'],
        'std': df_describe.loc['std'],
        'mean_theoretical': mean_theoretical,
        'std_theoretical': std_theoretical,
        'abs_mean_diff': abs_mean_diff,
        'abs_std_diff': abs_std_diff
    }, index=df_describe.columns)

    # Print the comparison DataFrame
    print(df_comparison)
    return df_comparison
    # END SOLUTION


def part2_step4(df2_students, df2_scores, ):
    # BEGIN SOLUTION
    # Define the maximum scores for each assignment and exam
    max_scores = {
        'Hw1': 50,
        'Hw2': 100,
        'Hw3': 40,
        'Hw4': 60,
        'Hw5': 50,
        'Exam1': 100,
        'Exam2': 50,
        'Exam3': 60,
        'Exam4': 50
    }

    # Calculate the scaled scores for each assignment and exam
    df_scaled_scores = (df2_scores / max_scores) * 100

    # Combine the scaled scores with the student information
    df_combined = pd.concat([df2_students, df_scaled_scores], axis=1)
    df_combined = df_combined.round()
   
    # Print the combined DataFrame
    print(df_combined)
    return df_combined
    # END SOLUTION


def part2_step5():
    # BEGIN SOLUTION
    df2_step5 = pd.read_csv("part2_step5-input.csv")
    # Fill missing values with 0
    df = df2_step5.fillna(0)
    # Find students with AI issues
    ai_students = df[['username', 'first_name', 'last_name']].copy()
    ai_students['AI_count'] = df.loc[:, 'Hw1':'Exam4'].apply(lambda x: x.str.contains('AI_ISSUE', na=False).sum(), axis=1)

    # Filter rows with AI issues
    ai_students = ai_students[ai_students['AI_count'] > 0]

    # Reset the index
    ai_students = ai_students.reset_index(drop=True)

    # Print the final DataFrame
    print(ai_students)
    return ai_students
    # END SOLUTION


def part2_step6():
    # BEGIN SOLUTION
    df = pd.read_csv("part2_step5-input.csv")

    # Replace 'AI_ISSUE' with 0
    df.replace('AI_ISSUE', 0, inplace=True)

    # Convert homework and exam columns to float
    homework_cols = ['Hw1', 'Hw2', 'Hw3', 'Hw4', 'Hw5']
    exam_cols = ['Exam1', 'Exam2', 'Exam3', 'Exam4']
    df[homework_cols + exam_cols] = df[homework_cols + exam_cols].astype(float)

    df[homework_cols] = df[homework_cols].apply(lambda x: x.fillna(x.mean()), axis=1)
    df[homework_cols] = df[homework_cols].round()

    # Replace missing exams with the average of other exams
    df[exam_cols] = df[exam_cols].apply(lambda x: x.fillna(x.mean()), axis=1)
    df[exam_cols] = df[exam_cols].round()
    # Calculate the grade
    hw_weight = 0.05
    exam1_3_weight = 0.2
    exam4_weight = 0.15
    df['Grade'] = (df[homework_cols].mean(axis=1) * hw_weight * 5 +
                df[exam_cols[:3]].mean(axis=1) * exam1_3_weight * 3 +
                df['Exam4'] * exam4_weight).round()

    # Map the grade to a letter grade
    df['LetterGrade'] = df['Grade'].apply(lambda grade: 'A' if grade >= 80
                                        else 'B' if grade >= 70
                                        else 'C' if grade >= 50
                                        else 'D' if grade >= 40
                                        else 'F')

    mean_row = pd.DataFrame(df.select_dtypes(include=np.number).mean().round(), columns=['mean']).T
    std_row = pd.DataFrame(df.select_dtypes(include=np.number).std().round(), columns=['mean']).T
    df = pd.concat([df, mean_row], sort=False)
    df = pd.concat([df, std_row], sort=False)


    # Reorder the columns
    df = df[['username', 'first_name', 'last_name', 'Hw1', 'Hw2', 'Hw3', 'Hw4', 'Hw5',
            'Exam1', 'Exam2', 'Exam3', 'Exam4', 'Grade', 'LetterGrade']]

    # Display the DataFrame
    return df
    # END SOLUTION
