import pandas as pd
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from datetime import datetime
from collections import Counter
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Read the following link and complete this homework. https://www.codemag.com/Article/1711091/Implementing-Machine-Learning-Using-Python-and-Scikit-learn

# Make sure to install scikit-learn and Pandas

def step1():
    """
    # Step 1: Getting the Titanic Dataset
    Return a dataframe containing the Titantic dataset from the following URL
    # URL: https://gist.githubusercontent.com/mkzia/aa4f293661dba857b8c4459c0095ac95/raw/8075037f6f7689a1786405c1bc8ea9471d3aa9c3/train.csv

    """
    # BEGIN SOLUTION
    url = "https://gist.githubusercontent.com/mkzia/aa4f293661dba857b8c4459c0095ac95/raw/8075037f6f7689a1786405c1bc8ea9471d3aa9c3/train.csv"
    df = pd.read_csv(url)
    return df
    # END SOLUTION
    # return df


def step2(df):
    """
    # Step 2: Clean data
    Modify df to drop the following columns:
    PassengerId
    Name
    Ticket
    Cabin
    Hint: Just pass all the columns to the .drop() method as an array
    return dataframe
    """
    # BEGIN SOLUTION
    df = df.drop('PassengerId', axis=1)
    df = df.drop('Name',        axis=1)
    df = df.drop('Ticket',      axis=1)
    df = df.drop('Cabin',       axis=1)
    return df

    # END SOLUTION
    # return df


def step3(df):
    """
    # Step 3: Drop NaNs and reindex
    You want to reindex so your index does not have missing values after you drop the NaNs. Remember, index is used 
    to access a row. Notice how many rows you dropped!
    Modify df to drop NaNs and reindex
    return dataframe
    """
    # BEGIN SOLUTION
    df = df.dropna()                
    df = df.reset_index(drop=True)  
    return df
    # END SOLUTION
    # return df


def step4(df):
    """
    # Step 4: Encoding the Non-Numeric Fields
    Encode text fields to numbers
    Modify df to encode Sex and Embarked to encoded values.
    return dataframe
    """
    # BEGIN SOLUTION
    label_encoder = preprocessing.LabelEncoder()
    sex_encoded = label_encoder.fit_transform(df["Sex"])
    df['Sex'] = sex_encoded
    embarked_encoded = label_encoder.fit_transform(df["Embarked"])
    df['Embarked'] = embarked_encoded
    return df
    # END SOLUTION
    # return df


def step5(df):
    """
    # Step 5: Making Fields Categorical
    Turn values that are not continues values into categorical values
    Modify df to make Pclass, Sex, Embarked, and Survived a categorical field
    return dataframe
    """
    # BEGIN SOLUTION
    df["Pclass"]   = pd.Categorical(df["Pclass"])
    df["Sex"]      = pd.Categorical(df["Sex"])
    df["Embarked"] = pd.Categorical(df["Embarked"])
    df["Survived"] = pd.Categorical(df["Survived"])
    return df
    # END SOLUTION
    # return df


def step6(df):
    """
    1. Split dataframe into feature and label
    2. Do train and test split; USE: random_state = 1
    4. Use LogisticRegression() for classification
    3. Return accuracy and confusion matrix

    Use  metrics.confusion_matrix to calculate the confusion matrix
    # https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
    # IMPORTANT !!!! 
    # https://stackoverflow.com/questions/56078203/why-scikit-learn-confusion-matrix-is-reversed

    From the confusion matrix get TN, FP, FN, TP

    return --> accuracy, TN, FP, FN, TP; 
    Hint: round accuracy to 4 decimal places

    """
    # BEGIN SOLUTION

    features= df.drop(columns=['Survived'])
    label    = df['Survived']
    train_features,test_features, train_label,test_label = train_test_split(
    features,
    label,
    random_state = 1,
    stratify = df["Survived"])
    log_regress = linear_model.LogisticRegression()
    log_regress.fit(X = train_features ,
    y = train_label)   
    preds = log_regress.predict(X=test_features)
    log_regress.score(X = test_features, y = test_label)
    confusion_matrix= metrics.confusion_matrix(y_true= test_label, y_pred= preds)
    TN, FP, FN, TP = confusion_matrix.flatten()
    accuracy = round((TP+TN)/(TP+FP+FN+TN),4)
    return accuracy, TN, FP, FN, TP; 
    # END SOLUTION

def ex1():
    """
    YOU CANNOT USE PANDAS OR CSV MODULE to solve the following problems
    Reproduce ex1.tsv from 'AdmissionsCorePopulatedTable.txt'
    https://mkzia.github.io/eas503-notes/sql/sql_6_conditionals.html#conditionals
    Separate the columns by a tab
    """

    # BEGIN SOLUTION

    with open('AdmissionsCorePopulatedTable.txt', 'r') as f:
        lines = f.readlines()

    admission_dates = [line.strip().split('\t')[2].split(' ')[0] for line in lines[1:] if line.strip()]
    admission_months = [datetime.strptime(date, '%Y-%m-%d').strftime('%B') for date in admission_dates]
    month_counts = Counter(admission_months)

    sorted_counts = sorted(month_counts.items(), key=lambda x: (-x[1], x[0]))

    with open("ex1.tsv", "w") as tsv_file:
        # Write the header line
        tsv_file.write("AdmissionMonth\tAdmissionCount\n")
        
        # Write the data rows
        for month, count in sorted_counts:
            line = f"{month}\t{count}\n"
            tsv_file.write(line)
  
    # END SOLUTION


def ex2():
    """
    YOU CANNOT USE PANDAS OR CSV MODULE to solve the following problems
    Repeat ex1 but add the Quarter column 
    This is the last SQL query on https://mkzia.github.io/eas503-notes/sql/sql_6_conditionals.html#conditionals
    Hint: https://stackoverflow.com/questions/60624571/sort-list-of-month-name-strings-in-ascending-order
    """

    # BEGIN SOLUTION

    with open('AdmissionsCorePopulatedTable.txt', 'r') as f:
       lines = f.readlines()

    admission_dates = [line.strip().split('\t')[2].split(' ')[0] for line in lines[1:] if line.strip()]
    admission_months = [datetime.strptime(date, '%Y-%m-%d').strftime('%B') for date in admission_dates]
    month_counts = Counter(admission_months)
    sorted_counts = sorted(month_counts.items(), key=lambda x: (datetime.strptime(x[0], '%B').month, x[1]))

    quarters = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3', 'Q4', 'Q4', 'Q4']

    output_list = [(quarter, month, count) for (month, count), quarter in zip(sorted_counts, quarters)]

    # Open the file for writing
    with open("ex2.tsv", "w") as tsv_file:
        # Write the header line
        tsv_file.write("Quarter\tAdmissionMonth\tAdmissionCount\n")
        
        # Write the data rows
        for row in output_list:
            line = "\t".join(str(item) for item in row) + "\n"
            tsv_file.write(line) 
  
    # END SOLUTION


def ex3():
    """
    YOU CANNOT USE PANDAS OR CSV MODULE to solve the following problems
    Reproduce 
    SELECT
        LabsCorePopulatedTable.PatientID,
        PatientCorePopulatedTable.PatientGender,
        LabName,
        LabValue,
        LabUnits,
        CASE
            WHEN PatientCorePopulatedTable.PatientGender = 'Male'
            AND LabValue BETWEEN 0.7
            AND 1.3 THEN 'Normal'
            WHEN PatientCorePopulatedTable.PatientGender = 'Female'
            AND LabValue BETWEEN 0.6
            AND 1.1 THEN 'Normal'
            ELSE 'Out of Range'
        END Interpretation
    FROM
        LabsCorePopulatedTable
        JOIN PatientCorePopulatedTable ON PatientCorePopulatedTable.PatientID = LabsCorePopulatedTable.PatientID
    WHERE
        LabName = 'METABOLIC: CREATININE'
    ORDER BY
        - LabValue

    using PatientCorePopulatedTable.txt and LabsCorePopulatedTable

    **** ADD  LabDateTime
    **** SORT BY Patient ID and then LabDateTime in ascending order 
    """

    with open('LabsCorePopulatedTable.txt', 'r') as labs_file:
        labs_data = labs_file.readlines()

    # Read data from 'PatientCorePopulatedTable.txt'
    with open('PatientCorePopulatedTable.txt', 'r') as patient_file:
        patient_data = patient_file.readlines()

    # Remove newline characters and split the data by tabs
    labs_data = [line.strip().split('\t') for line in labs_data]
    patient_data = [line.strip().split('\t') for line in patient_data]

    # Filter labs data for LabName = 'METABOLIC: CREATININE'
    labs_filtered = [line for line in labs_data if line[2] == 'METABOLIC: CREATININE']

    # Create a dictionary to store patient data with PatientID as the key
    patients_dict = {line[0]: line for line in patient_data}

    # Merge labs and patient data based on PatientID
    merged_data = []
    for lab in labs_filtered:
        patient_id = lab[0]
        lab_value = float(lab[3])
        lab_date = lab[5]

        if patient_id in patients_dict:
            patient = patients_dict[patient_id]
            gender = patient[1]
            interpretation = 'Normal' if (gender == 'Male' and 0.7 <= lab_value <= 1.3) or (gender == 'Female' and 0.6 <= lab_value <= 1.1) else 'Out of Range'

            merged_data.append([patient_id, gender, lab[2], lab[3], lab[4], lab_date, interpretation])

    # Sort the merged data by PatientID and LabDateTime in ascending order
    merged_data.sort(key=lambda x: (x[0], x[5]))

   # Call the function and assign the result to a variable
    headers = ["PatientID", "PatientGender", "LabName", "LabValue", "LabUnits", "LabDateTime", "Interpretation"]
    with open("ex3.tsv", "w") as tsv_file:
        # Write the header line
        header_line = "\t".join(headers) + "\n"
        tsv_file.write(header_line)

        # Write the data rows
        for row in merged_data:
            line = "\t".join(str(item) for item in row) + "\n"
            tsv_file.write(line)



def ex4():
    """
    YOU CANNOT USE PANDAS OR CSV MODULE to solve the following problems
    Reproduce this
    WITH AGE AS (
        SELECT 
            PATIENTID,
            ROUND((JULIANDAY('NOW') - JULIANDAY(PATIENTDATEOFBIRTH))/365.25) AGE
        FROM 
            PATIENTCOREPOPULATEDTABLE
    )
    SELECT 
        CASE 
            WHEN AGE < 18 THEN 'YOUTH'
            WHEN AGE BETWEEN 18 AND 35 THEN 'YOUNG ADULT'
            WHEN AGE BETWEEN 36 AND 55 THEN 'ADULT'
            WHEN AGE >= 56 THEN 'SENIOR'
        END AGE_RANGE,
        COUNT(*) AGE_RANGE_COUNT
    FROM 
        AGE
    GROUP BY AGE_RANGE
    ORDER BY AGE

    ****** VERY IMPORTANT: Use the Date: 2022-12-11 as today's date!!!! VERY IMPORTANT otherwise your result will change everyday!
    ****** VERY IMPORTANT divide the number of days by 365.25; to get age do math.floor(delta.days/365.25), where delta days is now-dob

    """
    # BEGIN SOLUTION

    # Define today's date
    today = datetime.strptime('2022-12-11', '%Y-%m-%d')
    result = []
    header = False
    with open('PatientCorePopulatedTable.txt', 'r') as f:
        age_range_counts = {'YOUTH': 0, 'YOUNG ADULT': 0, 'ADULT': 0, 'SENIOR': 0}
        for line in f:
            if not header:
                header=line.strip().split('\t')
                continue
            if line.strip():
                line = line.strip().split('\t')
                line = line[2]
                date = line.split(' ' )
                actual_date =date[0]
                actual_date=datetime.strptime(actual_date, '%Y-%m-%d')
                new=today-actual_date
                age_years=int((new).days / (365.24))
                if age_years < 18:
                    age_range = 'YOUTH'
                elif age_years > 17 and age_years < 36:
                    age_range = 'YOUNG ADULT'
                elif age_years >= 37 and age_years < 56:
                    age_range = 'ADULT'
                elif age_years >= 56:
                    age_range = 'SENIOR'
                age_range_counts[age_range] += 1
    for age_range, count in age_range_counts.items():
        if age_range != 'YOUTH':
            result.append((age_range, count))
    data = result
    with open("ex4.tsv", "w") as tsv_file:
        # Write the header line
        header_line = "AGE_RANGE\tAGE_RANGE_COUNT\n"
        tsv_file.write(header_line)

        # Write the data rows
        for row in data:
            line = "\t".join(str(item) for item in row) + "\n"
            tsv_file.write(line)      
    # END SOLUTION