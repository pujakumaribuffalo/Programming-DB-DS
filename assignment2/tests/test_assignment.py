import unittest
import os
import assignment
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestAssignment(unittest.TestCase):
    def setUp(self):
        self.assignment = assignment

    @weight(3)
    @visibility('visible')
    @number("eas503_27.1")
    def test_eas503_ex27_1(self):
        value = self.assignment.eas503_ex27('March', 21)
        self.assertEqual('Spring', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_27.2")
    def test_eas503_ex27_2(self):
        value = self.assignment.eas503_ex27('June', 21)
        self.assertEqual('Summer', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_27.3")
    def test_eas503_ex27_3(self):
        value = self.assignment.eas503_ex27('November', 21)
        self.assertEqual('Fall', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_27.4")
    def test_eas503_ex27_4(self):
        value = self.assignment.eas503_ex27('January', 21)
        self.assertEqual('Winter', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_27.5")
    def test_eas503_ex27_5(self):
        value = self.assignment.eas503_ex27('April', 21)
        self.assertEqual('Spring', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_27.6")
    def test_eas503_ex27_6(self):
        value = self.assignment.eas503_ex27('July', 21)
        self.assertEqual('Summer', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_27.7")
    def test_eas503_ex27_7(self):
        value = self.assignment.eas503_ex27('September', 21)
        self.assertEqual('Summer', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_27.8")
    def test_eas503_ex27_8(self):
        value = self.assignment.eas503_ex27('October', 21)
        self.assertEqual('Fall', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_28.1")
    def test_eas503_ex28_1(self):
        value = self.assignment.eas503_ex28(1800)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_28.2")
    def test_eas503_ex28_2(self):
        value = self.assignment.eas503_ex28(1900)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_28.3")
    def test_eas503_ex28_3(self):
        value = self.assignment.eas503_ex28(1600)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_28.4")
    def test_eas503_ex28_4(self):
        value = self.assignment.eas503_ex28(2000)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_29.1")
    def test_eas503_ex29_1(self):
        value = self.assignment.eas503_ex29(5, 24, 1962)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_29.2")
    def test_eas503_ex29_2(self):
        value = self.assignment.eas503_ex29(9, 31, 2000)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_29.3")
    def test_eas503_ex29_3(self):
        value = self.assignment.eas503_ex29(2, 29, 2000)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_29.4")
    def test_eas503_ex29_4(self):
        value = self.assignment.eas503_ex29(2, 29, 1800)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_30.1")
    def test_eas503_ex30_1(self):
        value = self.assignment.eas503_ex30(9, 31, 2000)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_30.2")
    def test_eas503_ex30_2(self):
        value = self.assignment.eas503_ex30(2, 13, 2020)
        self.assertEqual(44, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_30.3")
    def test_eas503_ex30_3(self):
        value = self.assignment.eas503_ex30(2, 29, 1800)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_30.4")
    def test_eas503_ex30_4(self):
        value = self.assignment.eas503_ex30(7, 26, 2020)
        self.assertEqual(208, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_31.01")
    def test_eas503_ex31_01(self):
        value = self.assignment.eas503_ex31('ABC123')
        self.assertEqual('Older/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_31.02")
    def test_eas503_ex31_02(self):
        value = self.assignment.eas503_ex31('GHE952')
        self.assertEqual('Older/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_31.03")
    def test_eas503_ex31_03(self):
        value = self.assignment.eas503_ex31('1934ABT')
        self.assertEqual('Newer/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_31.04")
    def test_eas503_ex31_04(self):
        value = self.assignment.eas503_ex31('bTR342')
        self.assertEqual('Invalid', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_31.05")
    def test_eas503_ex31_05(self):
        value = self.assignment.eas503_ex31('MHR621')
        self.assertEqual('Older/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_31.06")
    def test_eas503_ex31_06(self):
        value = self.assignment.eas503_ex31('POR208')
        self.assertEqual('Older/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_31.07")
    def test_eas503_ex31_07(self):
        value = self.assignment.eas503_ex31('1972BNT')
        self.assertEqual('Newer/Valid', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_31.08")
    def test_eas503_ex31_08(self):
        value = self.assignment.eas503_ex31('cRA542')
        self.assertEqual('Invalid', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_31.09")
    def test_eas503_ex31_09(self):
        value = self.assignment.eas503_ex31('1900bnT')
        self.assertEqual('Invalid', value)


    @weight(3)
    @visibility('visible')
    @number("eas503_31.10")
    def test_eas503_ex31_10(self):
        value = self.assignment.eas503_ex31('AS345f2')
        self.assertEqual('Invalid', value)

    @weight(3)
    @visibility('visible')
    @number("eas503_31.11")
    def test_eas503_ex31_11(self):
        value = self.assignment.eas503_ex31('Ghe952')
        self.assertEqual('Invalid', value)


    @weight(3)
    @visibility('visible')
    @number("eas503_32.1")
    def test_eas503_ex32_1(self):
        value = self.assignment.eas503_ex32('06/10/1960')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_32.2")
    def test_eas503_ex32_2(self):
        value = self.assignment.eas503_ex32('06/08/1948')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_32.3")
    def test_eas503_ex32_3(self):
        value = self.assignment.eas503_ex32('05/08/1940')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_32.4")
    def test_eas503_ex32_4(self):
        value = self.assignment.eas503_ex32('03/12/1948')
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_32.5")
    def test_eas503_ex32_5(self):
        value = self.assignment.eas503_ex32('02/12/1956')
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_32.6")
    def test_eas503_ex32_6(self):
        value = self.assignment.eas503_ex32('12/12/1990')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("eas503_33.01")
    def test_eas503_ex33_01(self):
        value = self.assignment.eas503_ex33('test1234')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("eas503_33.02")
    def test_eas503_ex33_02(self):
        value = self.assignment.eas503_ex33('password123')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("eas503_33.03")
    def test_eas503_ex33_03(self):
        value = self.assignment.eas503_ex33('SuperPasswrd90')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("eas503_33.04")
    def test_eas503_ex33_04(self):
        value = self.assignment.eas503_ex33('letmein!')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("eas503_33.05")
    def test_eas503_ex33_05(self):
        value = self.assignment.eas503_ex33('Password123@!')
        self.assertEqual(True, value)

    @weight(1)
    @visibility('visible')
    @number("eas503_33.06")
    def test_eas503_ex33_06(self):
        value = self.assignment.eas503_ex33('InWard@1234')
        self.assertEqual(True, value)

    @weight(1)
    @visibility('visible')
    @number("eas503_33.07")
    def test_eas503_ex33_07(self):
        value = self.assignment.eas503_ex33('Test3451')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("eas503_33.08")
    def test_eas503_ex33_08(self):
        value = self.assignment.eas503_ex33('AnandTech!892')
        self.assertEqual(True, value)

    @weight(1)
    @visibility('visible')
    @number("eas503_33.09")
    def test_eas503_ex33_09(self):
        value = self.assignment.eas503_ex33('aaaaaaaaaaaaaa')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("eas503_33.10")
    def test_eas503_ex33_10(self):
        value = self.assignment.eas503_ex33('12345!')
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_34.1")
    def test_eas503_ex34_1(self):
        value = self.assignment.eas503_ex34('This is a test sentence!')
        self.assertEqual(4, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_34.2")
    def test_eas503_ex34_2(self):
        value = self.assignment.eas503_ex34('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        self.assertEqual(5.46, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_35.1")
    def test_eas503_ex35_1(self):
        value = self.assignment.eas503_ex35('ex35_data.txt')
        self.assertEqual((50, 643, 4298), value)

    @weight(3)
    @visibility('visible')
    @number("eas503_36.1")
    def test_eas503_ex36_1(self):
        value = self.assignment.eas503_ex36(0.06)
        self.assertEqual(12, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_36.2")
    def test_eas503_ex36_2(self):
        value = self.assignment.eas503_ex36(0.1)
        self.assertEqual(8, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_37.1")
    def test_eas503_ex37_1(self):
        value = self.assignment.eas503_ex37(15)
        self.assertEqual(17, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_37.2")
    def test_eas503_ex37_2(self):
        value = self.assignment.eas503_ex37(35)
        self.assertEqual(13, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_37.3")
    def test_eas503_ex37_3(self):
        value = self.assignment.eas503_ex37(12)
        self.assertEqual(9, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_37.4")
    def test_eas503_ex37_4(self):
        value = self.assignment.eas503_ex37(27)
        self.assertEqual(111, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_38.1")
    def test_eas503_ex38_1(self):
        value = self.assignment.eas503_ex38(2)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_38.2")
    def test_eas503_ex38_2(self):
        value = self.assignment.eas503_ex38(3)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_38.3")
    def test_eas503_ex38_3(self):
        value = self.assignment.eas503_ex38(5)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_38.4")
    def test_eas503_ex38_4(self):
        value = self.assignment.eas503_ex38(25)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_39.1")
    def test_eas503_ex39_1(self):
        value = self.assignment.eas503_ex39(5)
        self.assertEqual([3, 5], value)

    @weight(3)
    @visibility('visible')
    @number("eas503_39.2")
    def test_eas503_ex39_2(self):
        value = self.assignment.eas503_ex39(25)
        self.assertEqual([3, 5, 7, 11, 13, 17, 19, 23], value)

    @weight(3)
    @visibility('visible')
    @number("eas503_40.1")
    def test_eas503_ex40_1(self):
        value = self.assignment.eas503_ex40(25, 75)
        self.assertEqual(25, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_40.2")
    def test_eas503_ex40_2(self):
        value = self.assignment.eas503_ex40(3, 13)
        self.assertEqual(1, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_40.3")
    def test_eas503_ex40_3(self):
        value = self.assignment.eas503_ex40(24, 62)
        self.assertEqual(2, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_40.4")
    def test_eas503_ex40_4(self):
        value = self.assignment.eas503_ex40(24, 48)
        self.assertEqual(24, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_41.1")
    def test_eas503_ex41_1(self):
        value = self.assignment.eas503_ex41('ex41_data.txt')
        self.assertEqual(('student733', 86.2, 'student202', 65.4), value)

    @weight(3)
    @visibility('visible')
    @number("eas503_42.1")
    def test_eas503_ex42_1(self):
        import random
        random.seed(1234)
        data = [random.randint(50, 150) for ele in range(100)]
        data[45] = 1
        data[46] = 2
        data[90] = 250
        data[34] = 300

        result = [50, 50, 51, 52, 52, 52, 53, 53, 54,
                  55, 55, 55, 55, 56, 58, 58, 59, 59, 59, 60, 61, 61,
                  61, 62, 64, 64, 64, 68, 68, 68, 69, 69, 69, 70, 71,
                  72, 73, 75, 77, 80, 81, 81, 84, 84, 84, 85, 88, 88, 89,
                  92, 94, 94, 95, 95, 98, 103, 106, 108, 108, 109, 109, 109,
                  110, 111, 111, 112, 113, 114, 115, 115, 117, 117, 119, 121,
                  124, 124, 125, 126, 128, 129, 132, 132, 133, 134, 135, 135,
                  135, 136, 138, 140, 141, 148, 148, 149, 149, 150]
        value = self.assignment.eas503_ex42(data, 2)

        self.assertEqual(result, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_42.2")
    def test_eas503_ex42_2(self):
        import random
        random.seed(1234)
        data = [random.randint(250, 450) for ele in range(100)]
        data[45] = 90
        data[46] = 76
        data[90] = 800
        data[34] = 900

        result = [251, 251, 253, 254, 254, 254, 256, 257, 258, 260,
                  260, 261, 263, 266, 267, 268, 269, 269, 271, 272, 273, 273,
                  275, 278, 279, 279, 286, 286, 286, 288, 289, 289, 291, 292,
                  295, 296, 301, 305, 310, 313, 313, 318, 319, 319, 320, 326,
                  327, 328, 335, 338, 338, 340, 340, 346, 356, 362, 366, 366,
                  368, 368, 369, 371, 373, 373, 374, 377, 378, 380, 381, 385,
                  385, 392, 392, 394, 398, 399, 400, 403, 407, 409, 415, 417,
                  418, 419, 420, 420, 421, 421, 422, 427, 431, 432, 446, 447, 449, 449]

        value = self.assignment.eas503_ex42(data, 2)
        self.assertEqual(result, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_43.1")
    def test_eas503_ex43_1(self):
        value = self.assignment.eas503_ex43(
            [21, 21, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 8])
        self.assertEqual([21, 1, 2, 3, 4, 5, 6, 7, 8], value)

    @weight(3)
    @visibility('visible')
    @number("eas503_43.2")
    def test_eas503_ex43_2(self):
        value = self.assignment.eas503_ex43(
            ['The', 'Man', 'The', 'Boy', 'Output', 'The', 'Man'])
        self.assertEqual(['The', 'Man', 'Boy', 'Output'], value)

    @weight(3)
    @visibility('visible')
    @number("eas503_44.1")
    def test_eas503_ex44_1(self):
        value = self.assignment.eas503_ex44(28)
        self.assertEqual([1, 2, 4, 7, 14], value)

    @weight(3)
    @visibility('visible')
    @number("eas503_44.2")
    def test_eas503_ex44_2(self):
        value = self.assignment.eas503_ex44(496)
        self.assertEqual([1, 2, 4, 8, 16, 31, 62, 124, 248], value)

    @weight(3)
    @visibility('visible')
    @number("eas503_45.1")
    def test_eas503_ex45_1(self):
        value = self.assignment.eas503_ex45(28)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_45.2")
    def test_eas503_ex45_2(self):
        value = self.assignment.eas503_ex45(76)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_45.3")
    def test_eas503_ex45_3(self):
        value = self.assignment.eas503_ex45(496)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_45.4")
    def test_eas503_ex45_4(self):
        value = self.assignment.eas503_ex45(512)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_46.1")
    def test_eas503_ex46_1(self):
        points = (
            (8, 3),
            (2, 10),
            (11, 3),
            (6, 6),
            (5, 8),
            (4, 12),
            (12, 1),
            (9, 4),
            (6, 9),
            (1, 14),
        )
        value = self.assignment.eas503_ex46(points)
        self.assertEqual((-1.11, 14.08), value)

    @weight(3)
    @visibility('visible')
    @number("eas503_46.2")
    def test_eas503_ex46_2(self):
        points = (
            (3, 8),
            (10, 2),
            (3, 11),
            (6, 6),
            (8, 5),
            (12, 4),
            (1, 12),
            (4, 9),
            (9, 6),
            (14, 1),
        )
        value = self.assignment.eas503_ex46(points)
        self.assertEqual((-0.79, 11.92), value)

    @weight(10)
    @visibility('visible')
    @number("eas503_47.1")
    def test_eas503_ex47_1(self):
        title = 'Cereal Yields (kg/ha)'
        header = ('Country', '1980', '1990', '2000', '2010')
        data = (
            ('China', 2937, 4321, 4752, 5527),
            ('Germany', 4225, 5411, 6453, 6718),
            ('United States', 3772, 4755, 5854, 6988),
        )
        if os.path.exists('ex47_1.txt'):
            os.remove('ex47_1.txt')
        self.assignment.eas503_ex47(title, header, data, 'ex47_1.txt')
        expected_result = open('ex47_1_solution.txt').read()
        actual_result = open('ex47_1.txt').read()
        self.assertEqual(expected_result, actual_result)

    @weight(10)
    @visibility('visible')
    @number("eas503_47.2")
    def test_eas503_ex47_2(self):
        title = 'MOST ACTIVE BY SHARE VOLUME'
        header = ('Symbol', 'Name', 'Last', 'Change', 'Share Volume')
        data = (
            ('AMD', 'Advanced Micro Devices, Inc.',
             '$120.88', '+4.27', '121,475,927'),
            ('AAPL', 'Apple Inc.', '$164.71', '+1.97', '80,725,613'),
            ('OPEN', 'Opendoor Technologies Inc', '$8.42', '-2.55', '53,559,847'),
            ('NVDA', 'NVIDIA Corporation', '$240.82', '+3.34', '49,046,544'),
            ('ZNGA', 'Zynga Inc.', '$9.18', '+0.37', '48,193,380'),
        )
        if os.path.exists('ex47_2.txt'):
            os.remove('ex47_2.txt')
        self.assignment.eas503_ex47(title, header, data, 'ex47_2.txt')
        expected_result = open('ex47_2_solution.txt').read()
        actual_result = open('ex47_2.txt').read()
        self.assertEqual(expected_result, actual_result)

    @weight(10)
    @visibility('visible')
    @number("eas503_47.3")
    def test_eas503_ex47_3(self):
        title = 'Student Grades'
        header = ('Student ID', 'Test1', 'Test2',
                  'Midterm', 'Quizzes', 'Final')
        data = (
            (2014255, 55, 78, 63, 50, 80),
            (2014301, 83, 45, 88, 52, 47),
            (2014023, 75, 70, 42, 74, 63),
            (2014155, 67, 87, 54, 87, 86),
        )
        if os.path.exists('ex47_3.txt'):
            os.remove('ex47_3.txt')
        self.assignment.eas503_ex47(title, header, data, 'ex47_3.txt')
        expected_result = open('ex47_3_solution.txt').read()
        actual_result = open('ex47_3.txt').read()
        self.assertEqual(expected_result, actual_result)

    @weight(3)
    @visibility('visible')
    @number("eas503_48.1")
    def test_eas503_ex48_1(self):
        value = self.assignment.eas503_ex48('ex48_data_1.txt')
        expected_value = 0.499675
        self.assertEqual(expected_value, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_48.2")
    def test_eas503_ex48_2(self):
        value = self.assignment.eas503_ex48('ex48_data_2.txt')
        expected_value = round(0.49939999999999996, 6)
        self.assertEqual(expected_value, round(value, 6))

    @weight(3)
    @visibility('visible')
    @number("eas503_48.3")
    def test_eas503_ex48_3(self):
        value = self.assignment.eas503_ex48('ex48_data_3.txt')
        expected_value = "The file does not have any valid number to compute the median"
        self.assertEqual(expected_value, value)