import unittest
import assignment
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestAssignment(unittest.TestCase):
    def setUp(self):
        self.assignment = assignment

    @weight(4)
    @visibility('visible')
    @number("01")
    def test_01(self):
        x = [1, 2, 3, 4]
        l1 = assignment.ListV2(x)
        expected_output = 2.5
        self.assertEqual(expected_output, l1.mean())

    @weight(4)
    @visibility('visible')
    @number("02")
    def test_02(self):
        x = [1, 2, 3, 4]
        l1 = assignment.ListV2(x)
        x.append(5)
        l1.append(5)
        expected_output = 3.0
        self.assertEqual(expected_output, l1.mean())

    @weight(4)
    @visibility('visible')
    @number("03")
    def test_03(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        data1=[ele.strip().split(',') for ele in open('testdata_1.txt')]
        print("data1", data1)
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)
        expected_output = """,StudentName,E1,E2,E3,E4,E5
0,student1,92,77,87,77,94
1,student2,74,93,88,67,85
2,student3,83,96,74,79,92
3,student4,100,72,83,85,66
4,student5,77,96,66,79,92
5,student6,100,86,84,70,71
6,student7,66,91,94,97,80
7,student8,97,86,75,69,88
8,student9,95,98,99,85,86
9,student10,78,76,73,88,86"""
        self.assertEqual(expected_output, df.__repr__())

    @weight(4)
    @visibility('visible')
    @number("04")
    def test_04(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)
        expected_output = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8', 'student9', 'student10']
        self.assertEqual(expected_output, df['StudentName'].values)

    @weight(4)
    @visibility('visible')
    @number("05")
    def test_05(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)
        expected_output = """,StudentName,E1
0,student1,92
1,student2,74
2,student3,83
3,student4,100
4,student5,77
5,student6,100
6,student7,66
7,student8,97
8,student9,95
9,student10,78"""
        self.assertEqual(expected_output, df[['StudentName', 'E1']].__repr__())

    @weight(4)
    @visibility('visible')
    @number("06")
    def test_06(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)
        output = df[['StudentName', 'E1']]
        expected_output = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8', 'student9', 'student10']
        self.assertEqual(expected_output, list(output['StudentName']))

    @weight(4)
    @visibility('visible')
    @number("07")
    def test_07(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)
        output = df[['StudentName', 'E1']]
        expected_output = ['92', '74', '83', '100', '77', '100', '66', '97', '95', '78']
        self.assertEqual(expected_output, list(output['E1']))

    @weight(4)
    @visibility('visible')
    @number("08")
    def test_08(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)
        expected_output = """,StudentName,E1,E2,E3,E4,E5
0,student2,74,93,88,67,85
1,student3,83,96,74,79,92
2,student4,100,72,83,85,66"""

        self.assertEqual(expected_output, df[1:4].__repr__())  # slice

    @weight(4)
    @visibility('visible')
    @number("09")
    def test_09(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        expected_output = {'StudentName': ['student2', 'student3', 'student4'],
                           'E1': ['74', '83', '100'],
                           'E2': ['93', '96', '72'],
                           'E3': ['88', '74', '83'],
                           'E4': ['67', '79', '85'],
                           'E5': ['85', '92', '66']}

        output = df[1:4]
        for key, value in expected_output.items():
            self.assertEqual(value, list(output[key]))

    @weight(4)
    @visibility('visible')
    @number("10")
    def test_10(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        expected_output = """,StudentName,E1,E2
0,student2,74,93
1,student3,83,96
2,student4,100,72"""

        self.assertEqual(expected_output, df[1:4, :3].__repr__())  # two slices

    @weight(4)
    @visibility('visible')
    @number("11")
    def test_11(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        expected_output = {'StudentName': ['student2', 'student3', 'student4'],
                           'E1': ['74', '83', '100'],
                           'E2': ['93', '96', '72']}

        output = df[1:4, :3]
        for key, value in expected_output.items():
            self.assertEqual(value, list(output[key]))

    @weight(4)
    @visibility('visible')
    @number("12")
    def test_12(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        expected_output = [92, 74, 83, 100, 77, 100, 66, 97, 95, 78]
        self.assertEqual(expected_output, df['E1'].values)

    @weight(4)
    @visibility('visible')
    @number("13")
    def test_13(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        expected_output = [169, 167, 179, 172, 173, 186, 157, 183, 193, 154]
        self.assertEqual(expected_output, (df['E1'] + df['E2']).values)

    @weight(4)
    @visibility('visible')
    @number("14")
    def test_14(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        expected_output = {'E1': 86.2, 'E2': 87.1, 'E3': 82.3, 'E4': 79.6, 'E5': 84.0}
        self.assertEqual(expected_output, df[['E1', 'E2', 'E3', 'E4', 'E5']].mean())

    @weight(4)
    @visibility('visible')
    @number("15")
    def test_15(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        expected_output = ['StudentName', 'E1', 'E2', 'E3', 'E4']
        self.assertEqual(expected_output, df.columns)

    @weight(4)
    @visibility('visible')
    @number("16")
    def test_16(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        expected_output = """,StudentName,E1,E2,E3,E4
0,student1,92,77,87,77
1,student2,74,93,88,67
2,student3,83,96,74,79
3,student4,100,72,83,85
4,student5,77,96,66,79
5,student6,100,86,84,70
6,student7,66,91,94,97
7,student8,97,86,75,69
8,student9,95,98,99,85
9,student10,78,76,73,88"""

        self.assertEqual(expected_output, df.__repr__())

    @weight(4)
    @visibility('visible')
    @number("17")
    def test_17(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        expected_output = df.loc(0)
        self.assertEqual(expected_output, df.loc(0))

    @weight(4)
    @visibility('visible')
    @number("18")
    def test_18(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        df.set_index(list(df['StudentName']))
        df.drop('StudentName')
        expected_output = """,E1,E2,E3,E4
student1,92,77,87,77
student2,74,93,88,67
student3,83,96,74,79
student4,100,72,83,85
student5,77,96,66,79
student6,100,86,84,70
student7,66,91,94,97
student8,97,86,75,69
student9,95,98,99,85
student10,78,76,73,88"""

        self.assertEqual(expected_output, df.__repr__())

    @weight(4)
    @visibility('visible')
    @number("19")
    def test_19(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        df.set_index(list(df['StudentName']))
        df.drop('StudentName')
        expected_output = """,E1,E2
student1,92,77
student2,74,93"""

        self.assertEqual(expected_output, df.loc((['student1', 'student2'], ['E1', 'E2'])).__repr__())

    @weight(4)
    @visibility('visible')
    @number("20")
    def test_20(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        df.set_index(list(df['StudentName']))
        df.drop('StudentName')
        expected_output = {'E1': [92, 74], 'E2': [77, 93]}

        output = df.loc((['student1', 'student2'], ['E1', 'E2']))
        for key, value in expected_output.items():
            self.assertEqual(value, list(output[key]))

    @weight(4)
    @visibility('visible')
    @number("21")
    def test_21(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        df.set_index(list(df['StudentName']))
        df.drop('StudentName')
        expected_output = ['E1', 'E2']
        output = df.loc((['student1', 'student2'], ['E1', 'E2']))
        self.assertEqual(expected_output, output.columns)

    @weight(4)
    @visibility('visible')
    @number("22")
    def test_22(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        df.set_index(list(df['StudentName']))
        df.drop('StudentName')
        output = df.loc((['student1', 'student2'], ['E1', 'E2']))
        expected_output = {'student1': 0, 'student2': 1}
        self.assertEqual(expected_output, output.index)

    @weight(4)
    @visibility('visible')
    @number("23")
    def test_23(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        df.set_index(list(df['StudentName']))
        df.drop('StudentName')
        output = df.loc((['student1', 'student2'], ['E1', 'E2']))
        expected_output = [('student1', (92, 77)), ('student2', (74, 93))]
        self.assertEqual(expected_output, output.iterrows())

    @weight(4)
    @visibility('visible')
    @number("24")
    def test_24(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        df.set_index(list(df['StudentName']))
        df.drop('StudentName')
        output = df.loc((['student1', 'student2'], ['E1', 'E2']))
        expected_output = {'E1': [92, 74], 'E2': [77, 93]}
        self.assertEqual(expected_output, dict(output.iteritems()))

    @weight(4)
    @visibility('visible')
    @number("25")
    def test_25(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        df.set_index(list(df['StudentName']))
        df.drop('StudentName')
        expected_output = [('student1', (92, 77, 87, 77)),
                           ('student2', (74, 93, 88, 67)),
                           ('student3', (83, 96, 74, 79)),
                           ('student4', (100, 72, 83, 85)),
                           ('student5', (77, 96, 66, 79)),
                           ('student6', (100, 86, 84, 70)),
                           ('student7', (66, 91, 94, 97)),
                           ('student8', (97, 86, 75, 69)),
                           ('student9', (95, 98, 99, 85)),
                           ('student10', (78, 76, 73, 88))]

        self.assertEqual(expected_output, df.iterrows())

    @weight(4)
    @visibility('visible')
    @number("26")
    def test_26(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        df.set_index(list(df['StudentName']))
        df.drop('StudentName')
        expected_output = {'E1': [92, 74, 83, 100, 77, 100, 66, 97, 95, 78],
                           'E2': [77, 93, 96, 72, 96, 86, 91, 86, 98, 76],
                           'E3': [87, 88, 74, 83, 66, 84, 94, 75, 99, 73],
                           'E4': [77, 67, 79, 85, 79, 70, 97, 69, 85, 88]}
        self.assertEqual(expected_output, dict(df.iteritems()))  # column wise

    @weight(4)
    @visibility('visible')
    @number("27")
    def test_27(self):
        columns = ('StudentName', 'E1', 'E2', 'E3', 'E4', 'E5')
        df = assignment.DataFrame(data=[ele.strip().split(',') for ele in open('testdata_1.txt')], columns=columns)

        for col in ['E1', 'E2', 'E3', 'E4', 'E5']:
            df.as_type(col, int)

        df.drop('E5')
        df.set_index(list(df['StudentName']))
        df.drop('StudentName')
        output = df.loc((['student1', 'student2', 'student3'], ['E1']))
        expected_output = [('student1', (92,)), ('student2', (74,)), ('student3', (83,))]
        self.assertEqual(expected_output, output.iterrows())
