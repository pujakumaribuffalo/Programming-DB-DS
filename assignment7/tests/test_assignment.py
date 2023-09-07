import unittest

import pandas as pd
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)

import assignment


class TestAssignment(unittest.TestCase):

    def setUp(self):
        self.assignment = assignment

    @weight(3)
    @visibility('visible')
    @number("01_df_degrees")
    def test_01_df_degrees(self):
        df_degrees_from_func = self.assignment.create_df_degrees('non_normalized.db')
        df_degrees_from_file = pd.read_csv("df_degrees.csv")
        self.assertEqual(df_degrees_from_func.equals(df_degrees_from_file), True)

    @weight(3)
    @visibility('visible')
    @number("02_df_exams")
    def test_02_df_exams(self):
        df_exams_from_func = self.assignment.create_df_exams('non_normalized.db')
        df_exams_from_file = pd.read_csv("df_exams.csv")
        self.assertEqual(df_exams_from_func.equals(df_exams_from_file), True)

    @weight(3)
    @visibility('visible')
    @number("03_df_students")
    def test_03_df_students(self):
        df_students_from_func = self.assignment.create_df_students('non_normalized.db')
        df_students_from_file = pd.read_csv("df_students.csv")
        self.assertEqual(df_students_from_func.equals(df_students_from_file), True)

    @weight(3)
    @visibility('visible')
    @number("04_df_studentexamscores")
    def test_04_df_studentexamscores(self):
        df_students = self.assignment.create_df_students('non_normalized.db')
        df_studentexamscores_from_func = self.assignment.create_df_studentexamscores('non_normalized.db', df_students)
        df_studentexamscores_from_file = pd.read_csv("df_studentexamscores.csv")
        self.assertEqual(df_studentexamscores_from_func.equals(df_studentexamscores_from_file), True)

    @weight(3)
    @visibility('visible')
    @number("ex1")
    def test_ex1(self):
        df_exams = self.assignment.create_df_exams('non_normalized.db')
        df_exams = self.assignment.ex1(df_exams)
        df_exams.reset_index(drop=True, inplace=True)
        df_exams_from_file = pd.read_csv("ex1.csv")
        self.assertEqual(df_exams.equals(df_exams_from_file), True)

    @weight(3)
    @visibility('visible')
    @number("ex2")
    def test_ex2(self):
        df_students = assignment.create_df_students('non_normalized.db')
        df = assignment.ex2(df_students)
        df.columns = ['Count']
        df_file = pd.read_csv("ex2.csv")
        df_file = df_file.iloc[1:]
        df_file.columns = ['Degree', 'Count']
        df_file.set_index('Degree', inplace=True)
        self.assertEqual(df_file.to_dict() == df.to_dict(), True)

    @weight(3)
    @visibility('visible')
    @number("ex3")
    def test_ex3(self):
        df_exams = self.assignment.create_df_exams('non_normalized.db')
        df_students = self.assignment.create_df_students('non_normalized.db')
        df_studentexamscores = self.assignment.create_df_studentexamscores('non_normalized.db', df_students)
        df_ex3 = self.assignment.ex3(df_studentexamscores, df_exams)
        df_from_file = pd.read_csv("ex3.csv", index_col=0)
        df_from_file['Year'] = df_from_file['Year'].astype('int32')
        df_ex3['Year'] = df_ex3['Year'].astype('int32')
        self.assertEqual(df_ex3.equals(df_from_file), True)

    @weight(3)
    @visibility('visible')
    @number("ex4")
    def test_ex4(self):
        df_students = self.assignment.create_df_students('non_normalized.db')
        df_studentexamscores = self.assignment.create_df_studentexamscores('non_normalized.db', df_students)
        df_ex4 = self.assignment.ex4(df_studentexamscores, df_students)
        df_from_file = pd.read_csv("ex4.csv", index_col=0)
        self.assertEqual(df_ex4.equals(df_from_file), True)

    @weight(3)
    @visibility('visible')
    @number("ex5")
    def test_ex5(self):
        df_students = self.assignment.create_df_students('non_normalized.db')
        df_studentexamscores = self.assignment.create_df_studentexamscores('non_normalized.db', df_students)
        df_ex5 = self.assignment.ex5(df_studentexamscores, df_students)
        df_from_file = pd.read_csv("ex5.csv")
        self.assertEqual(df_from_file.values.tolist(), df_ex5.values.tolist())

    @weight(3)
    @visibility('visible')
    @number("part2_step01")
    def test_part2_step01(self):
        df2_students = self.assignment.part2_step1()
        df2_from_file = pd.read_csv("part2_step1.csv")
        self.assertEqual(df2_from_file.values.tolist(), df2_students.values.tolist())

    @weight(3)
    @visibility('visible')
    @number("part2_step02")
    def test_part2_step02(self):
        df2_scores = self.assignment.part2_step2()
        df2_from_file = pd.read_csv("part2_step2.csv")
        self.assertEqual(df2_scores.values.tolist(), df2_from_file.values.tolist())

    @weight(3)
    @visibility('visible')
    @number("part2_step03")
    def test_part2_step03(self):
        df2_scores = self.assignment.part2_step2()
        df2_compare = self.assignment.part2_step3(df2_scores)
        df2_from_file = pd.read_csv("part2_step3.csv", index_col=0)
        self.assertEqual(df2_from_file.values.tolist(), df2_compare.values.tolist())

    @weight(3)
    @visibility('visible')
    @number("part2_step04")
    def test_part2_step04(self):
        df2_scores = self.assignment.part2_step2()
        df2_students = self.assignment.part2_step1()
        df2_score_sheet = self.assignment.part2_step4(df2_students, df2_scores)
        df2_from_file = pd.read_csv("part2_step4.csv")
        self.assertEqual(df2_from_file.values.tolist(), df2_score_sheet.values.tolist())

    @weight(3)
    @visibility('visible')
    @number("part2_step05")
    def test_part2_step05(self):
        df2_ai = self.assignment.part2_step5()
        df2_from_file = pd.read_csv("part2_step5.csv", index_col=0)
        self.assertEqual(df2_from_file.values.tolist(), df2_ai.values.tolist())

    @weight(3)
    @visibility('visible')
    @number("part2_step06")
    def test_part2_step06(self):
        df_grade = self.assignment.part2_step6()
        df2_from_file = pd.read_csv("part2_step6.csv", index_col=0)
        self.assertEqual(df2_from_file.values.tolist(), df_grade.values.tolist())
