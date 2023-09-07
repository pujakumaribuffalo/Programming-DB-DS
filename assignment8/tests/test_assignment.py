import unittest
import pandas as pd
import assignment
import sqlite3
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class Testassignment(unittest.TestCase):

    def setUp(self):
        self.assignment = assignment

    @weight(6)
    @visibility('visible')
    @number("step1")
    def test_step1(self):
        df_from_func = self.assignment.step1()
        df_from_file = pd.read_csv('step1_output.csv')
        assert df_from_func.equals(df_from_file) == True

    @weight(6)
    @visibility('visible')
    @number("step2")
    def test_step2(self):
        df_from_step1 = self.assignment.step1()
        df_from_func = self.assignment.step2(df_from_step1)
        df_from_file = pd.read_csv('step2_output.csv')
        assert df_from_func.equals(df_from_file) == True

    @weight(6)
    @visibility('visible')
    @number("step3")
    def test_step3(self):
        df_from_step1 = self.assignment.step1()
        df_from_step2 = self.assignment.step2(df_from_step1)
        df_from_func = self.assignment.step3(df_from_step2)
        df_from_file = pd.read_csv('step3_output.csv')
        assert df_from_func.equals(df_from_file) == True

    @weight(6)
    @visibility('visible')
    @number("step4")
    def test_step4(self):
        df_from_step1 = self.assignment.step1()
        df_from_step2 = self.assignment.step2(df_from_step1)
        df_from_step3 = self.assignment.step3(df_from_step2)
        df_from_func = self.assignment.step4(df_from_step3)
        df_from_file = pd.read_csv('step4_output.csv')
        df_from_file['Sex'] = df_from_file['Sex'].astype('int32')
        df_from_file['Embarked'] = df_from_file['Embarked'].astype('int32')
        df_from_func['Sex'] = df_from_file['Sex'].astype('int32')
        df_from_func['Embarked'] = df_from_file['Embarked'].astype('int32')
        assert df_from_func.equals(df_from_file) == True

    @weight(6)
    @visibility('visible')
    @number("step5")
    def test_step5(self):
        df_from_step1 = self.assignment.step1()
        df_from_step2 = self.assignment.step2(df_from_step1)
        df_from_step3 = self.assignment.step3(df_from_step2)
        df_from_step4 = self.assignment.step4(df_from_step3)
        df_from_func = self.assignment.step5(df_from_step4)
        df_from_file = pd.read_csv('step5_output.csv', skiprows=[0], header=None)

        df_from_file.columns = ['', 1]
        df_from_file.set_index('', inplace=True)
        df_from_file.columns = ['']

        df_from_func = pd.DataFrame(df_from_func.dtypes)
        df_from_func.columns = ['']

        assert df_from_func.equals(df_from_file) == True

    @weight(6)
    @visibility('visible')
    @number("step6")
    def test_step6(self):
        df_from_step1 = self.assignment.step1()
        df_from_step2 = self.assignment.step2(df_from_step1)
        df_from_step3 = self.assignment.step3(df_from_step2)
        df_from_step4 = self.assignment.step4(df_from_step3)
        df_from_step5 = self.assignment.step5(df_from_step4)
        accuracy, TN, FP, FN, TP = self.assignment.step6(df_from_step5)

        assert accuracy == 0.7978
        assert TN == 90
        assert FP == 16
        assert FN == 20
        assert TP == 52

    @weight(10)
    @visibility('visible')
    @number("ex1")
    def test_ex1(self):
        self.assignment.ex1()
        result_from_file = pd.read_csv('ex1.tsv')
        expected_from_file = pd.read_csv('ex1_solution.tsv')
        assert result_from_file.equals(expected_from_file) == True

    @weight(10)
    @visibility('visible')
    @number("ex2")
    def test_ex2(self):
        self.assignment.ex2()
        result_from_file = pd.read_csv('ex2.tsv')
        expected_from_file = pd.read_csv('ex2_solution.tsv')
        assert result_from_file.equals(expected_from_file) == True

    @weight(10)
    @visibility('visible')
    @number("ex3")
    def test_ex3(self):
        self.assignment.ex3()
        result_from_file = pd.read_csv('ex3.tsv')
        expected_from_file = pd.read_csv('ex3_solution.tsv')
        assert result_from_file.equals(expected_from_file) == True

    @weight(10)
    @visibility('visible')
    @number("ex4")
    def test_ex4(self):
        self.assignment.ex4()
        result_from_file = pd.read_csv('ex4.tsv')
        expected_from_file = pd.read_csv('ex4_solution.tsv')
        assert result_from_file.equals(expected_from_file) == True

