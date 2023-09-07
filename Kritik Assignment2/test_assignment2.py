
import unittest

class TestCSVFilter(unittest.TestCase):
    def test_filter_students(self):
        # Test Case 1
        input_file = 'input.csv'
        expected_output_file = 'output.csv'

        # Run the code to generate the actual output file
        actual_output_file = 'actual_output.csv3'
        filter_students(input_file, actual_output_file)

        # Compare the actual output file with the expected output file
        self.assertTrue(compare_files(actual_output_file, expected_output_file))

        

def filter_students(input_file, output_file):
   with open('input.csv', 'r') as file:
   contents = file.read()

# Split the data into lines
lines = contents.split('\n')

# Extract header and rows
header = lines[0]
rows = lines[1:]

# Create a new list for filtered rows
filtered_rows = []

# Iterate over each row
for row in rows:
    # Split the row into fields
    fields = row.split(',')

    
    year1 = int(fields[1].split('-')[0])  
    year2 = int(fields[2].split('-')[0])  

    # Calculate the difference between the years
    year_difference = abs(year2 - year1)

    # Check if the difference is less than or equal to 5
    if year_difference <= 5:
        # Add the row to the filtered list
        filtered_rows.append(row)

#filtered rows along with the header to output.csv
with open('output.csv', 'w') as file:
    file.write(header + '\n')
    file.write('\n'.join(filtered_rows))


def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                return False
        return True

if __name__ == '__main__':
    unittest.main()
