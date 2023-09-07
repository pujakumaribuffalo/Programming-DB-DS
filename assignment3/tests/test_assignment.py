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
    @number("eas503_ex49_01")
    def test_eas503_ex49_01(self):
        l_func, min_student = self.assignment.eas503_ex49('grades.txt')
        expected_value = 'student11,72,69,69,65,91'
        self.assertEqual(expected_value, min_student)

    @weight(3)
    @visibility('visible')
    @number("eas503_ex49_02")
    def test_eas503_ex49_02(self):
        l_func, min_student = self.assignment.eas503_ex49('grades.txt')
        lines = (
            'student45,83,74,99,76,95',
            'student46,96,83,79,89,71',
            'student47,70,85,94,73,74',
            'student48,99,72,92,65,87',
            'student49,78,93,99,77,85',
            'student50,96,91,76,72,66',
            'student51,94,86,77,91,96',
        )

        expected_value = 'student47,70,85,94,73,74'
        self.assertEqual(expected_value, min(lines, key=l_func))

    @weight(3)
    @visibility('visible')
    @number("eas503_ex49_03")
    def test_eas503_ex49_03(self):
        import types
        l_func, min_student = self.assignment.eas503_ex49('grades.txt')
        self.assertEqual(types.LambdaType, type(l_func))

    @weight(3)
    @visibility('visible')
    @number("eas503_ex50_01")
    def test_eas503_ex50_01(self):
        import types
        l_func, student_grades = self.assignment.eas503_ex50('grades.txt')
        expected_value = ['student1: B',
                          'student2: B',
                          'student3: B',
                          'student4: B',
                          'student5: B',
                          'student6: B',
                          'student7: C',
                          'student8: C',
                          'student9: B',
                          'student10: C',
                          'student11: C',
                          'student12: C',
                          'student13: B',
                          'student14: B',
                          'student15: C',
                          'student16: B',
                          'student17: B',
                          'student18: B',
                          'student19: C',
                          'student20: B',
                          'student21: B',
                          'student22: C',
                          'student23: B',
                          'student24: B',
                          'student25: A',
                          'student26: B',
                          'student27: C',
                          'student28: B',
                          'student29: B',
                          'student30: B',
                          'student31: B',
                          'student32: C',
                          'student33: B',
                          'student34: B',
                          'student35: B',
                          'student36: C',
                          'student37: B',
                          'student38: B',
                          'student39: C',
                          'student40: C',
                          'student41: B',
                          'student42: A',
                          'student43: B',
                          'student44: C',
                          'student45: B',
                          'student46: B',
                          'student47: C',
                          'student48: B',
                          'student49: B',
                          'student50: B',
                          'student51: B',
                          'student52: C',
                          'student53: B',
                          'student54: C',
                          'student55: A',
                          'student56: A',
                          'student57: B',
                          'student58: C',
                          'student59: B',
                          'student60: B',
                          'student61: B',
                          'student62: B',
                          'student63: B',
                          'student64: B',
                          'student65: C',
                          'student66: C',
                          'student67: C',
                          'student68: B',
                          'student69: B',
                          'student70: B',
                          'student71: B',
                          'student72: C',
                          'student73: B',
                          'student74: B',
                          'student75: B',
                          'student76: B',
                          'student77: B',
                          'student78: C',
                          'student79: B',
                          'student80: B',
                          'student81: B',
                          'student82: C',
                          'student83: B',
                          'student84: C',
                          'student85: C',
                          'student86: B',
                          'student87: A',
                          'student88: B',
                          'student89: C',
                          'student90: B',
                          'student91: B',
                          'student92: C',
                          'student93: C',
                          'student94: C',
                          'student95: A',
                          'student96: B',
                          'student97: A',
                          'student98: B',
                          'student99: C',
                          'student100: B']

        self.assertEqual(expected_value, list(student_grades))

    @weight(3)
    @visibility('visible')
    @number("eas503_ex50_02")
    def test_eas503_ex50_02(self):
        import types
        l_func, student_grades = self.assignment.eas503_ex50('grades.txt')
        self.assertEqual(types.LambdaType, type(l_func))

    @weight(3)
    @visibility('visible')
    @number("eas503_ex50_03")
    def test_eas503_ex50_03(self):
        l_func, student_grades = self.assignment.eas503_ex50('grades.txt')
        lines = (
            'student45,83,74,99,76,95',
            'student46,96,83,79,89,71',
            'student47,70,85,94,73,74',
            'student48,99,72,92,65,87',
            'student49,78,93,99,77,85',
            'student50,96,91,76,72,66',
            'student51,94,86,77,91,96',
        )

        expected_value = [
            'student45: B',
            'student46: B',
            'student47: C',
            'student48: B',
            'student49: B',
            'student50: B',
            'student51: B'
        ]

        self.assertEqual(expected_value, list(map(l_func, lines)))

    @weight(3)
    @visibility('visible')
    @number("eas503_ex51_01")
    def test_eas503_ex51_01(self):
        l_func, output = self.assignment.eas503_ex51('grades_dict.json')

        expected_value = [
            {'name': 'student2', 'test1': '100', 'test2': '90',
                'test3': '65', 'test4': '68', 'test5': '94'},
            {'name': 'student83', 'test1': '88', 'test2': '76',
                'test3': '65', 'test4': '97', 'test5': '82'},
            {'name': 'student31', 'test1': '90', 'test2': '87',
                'test3': '66', 'test4': '95', 'test5': '72'},
            {'name': 'student43', 'test1': '86', 'test2': '69',
                'test3': '66', 'test4': '70', 'test5': '74'},
            {'name': 'student47', 'test1': '93', 'test2': '78',
                'test3': '67', 'test4': '74', 'test5': '74'},
            {'name': 'student52', 'test1': '83', 'test2': '78',
                'test3': '67', 'test4': '71', 'test5': '65'},
            {'name': 'student37', 'test1': '91', 'test2': '78',
                'test3': '68', 'test4': '67', 'test5': '92'},
            {'name': 'student58', 'test1': '89', 'test2': '88',
                'test3': '68', 'test4': '79', 'test5': '79'},
            {'name': 'student63', 'test1': '85', 'test2': '66',
                'test3': '69', 'test4': '74', 'test5': '69'},
            {'name': 'student12', 'test1': '88', 'test2': '83',
                'test3': '71', 'test4': '89', 'test5': '73'},
            {'name': 'student85', 'test1': '76', 'test2': '100',
                'test3': '71', 'test4': '69', 'test5': '65'},
            {'name': 'student98', 'test1': '81', 'test2': '85',
                'test3': '71', 'test4': '89', 'test5': '76'},
            {'name': 'student17', 'test1': '86', 'test2': '98',
                'test3': '73', 'test4': '100', 'test5': '92'},
            {'name': 'student62', 'test1': '86', 'test2': '100',
                'test3': '73', 'test4': '99', 'test5': '76'},
            {'name': 'student69', 'test1': '93', 'test2': '95',
                'test3': '73', 'test4': '86', 'test5': '90'},
            {'name': 'student81', 'test1': '95', 'test2': '83',
                'test3': '74', 'test4': '75', 'test5': '81'},
            {'name': 'student93', 'test1': '95', 'test2': '97',
                'test3': '74', 'test4': '74', 'test5': '81'},
            {'name': 'student26', 'test1': '80', 'test2': '78',
                'test3': '75', 'test4': '69', 'test5': '87'},
            {'name': 'student34', 'test1': '93', 'test2': '88',
                'test3': '77', 'test4': '67', 'test5': '93'},
            {'name': 'student14', 'test1': '85', 'test2': '97',
                'test3': '78', 'test4': '67', 'test5': '99'},
            {'name': 'student79', 'test1': '91', 'test2': '94',
                'test3': '78', 'test4': '83', 'test5': '92'},
            {'name': 'student25', 'test1': '77', 'test2': '86',
                'test3': '79', 'test4': '70', 'test5': '92'},
            {'name': 'student55', 'test1': '91', 'test2': '76',
                'test3': '79', 'test4': '65', 'test5': '66'},
            {'name': 'student70', 'test1': '100', 'test2': '71',
                'test3': '79', 'test4': '99', 'test5': '78'},
            {'name': 'student80', 'test1': '98', 'test2': '85',
                'test3': '79', 'test4': '91', 'test5': '92'},
            {'name': 'student13', 'test1': '95', 'test2': '72',
                'test3': '80', 'test4': '73', 'test5': '84'},
            {'name': 'student35', 'test1': '75', 'test2': '89',
                'test3': '80', 'test4': '93', 'test5': '74'},
            {'name': 'student20', 'test1': '68', 'test2': '68',
                'test3': '81', 'test4': '74', 'test5': '76'},
            {'name': 'student50', 'test1': '94', 'test2': '68',
                'test3': '81', 'test4': '69', 'test5': '89'},
            {'name': 'student66', 'test1': '91', 'test2': '92',
                'test3': '81', 'test4': '79', 'test5': '69'},
            {'name': 'student1', 'test1': '73', 'test2': '91',
                'test3': '82', 'test4': '90', 'test5': '93'},
            {'name': 'student100', 'test1': '79', 'test2': '79',
                'test3': '82', 'test4': '71', 'test5': '87'},
            {'name': 'student5', 'test1': '86', 'test2': '93',
                'test3': '83', 'test4': '94', 'test5': '94'},
            {'name': 'student16', 'test1': '81', 'test2': '95',
                'test3': '83', 'test4': '87', 'test5': '95'},
            {'name': 'student19', 'test1': '70', 'test2': '70',
                'test3': '83', 'test4': '99', 'test5': '97'},
            {'name': 'student61', 'test1': '65', 'test2': '76',
                'test3': '83', 'test4': '75', 'test5': '68'},
            {'name': 'student91', 'test1': '79', 'test2': '100',
                'test3': '83', 'test4': '66', 'test5': '69'},
            {'name': 'student96', 'test1': '99', 'test2': '93',
                'test3': '83', 'test4': '75', 'test5': '85'},
            {'name': 'student21', 'test1': '74', 'test2': '73',
                'test3': '84', 'test4': '84', 'test5': '69'},
            {'name': 'student46', 'test1': '92', 'test2': '83',
                'test3': '84', 'test4': '69', 'test5': '90'},
            {'name': 'student22', 'test1': '65', 'test2': '87',
                'test3': '85', 'test4': '78', 'test5': '98'},
            {'name': 'student23', 'test1': '88', 'test2': '95',
                'test3': '85', 'test4': '67', 'test5': '93'},
            {'name': 'student72', 'test1': '85', 'test2': '66',
                'test3': '85', 'test4': '78', 'test5': '75'},
            {'name': 'student82', 'test1': '77', 'test2': '100',
                'test3': '85', 'test4': '65', 'test5': '80'},
            {'name': 'student88', 'test1': '77', 'test2': '87',
                'test3': '85', 'test4': '90', 'test5': '78'},
            {'name': 'student18', 'test1': '65', 'test2': '78',
                'test3': '86', 'test4': '69', 'test5': '98'},
            {'name': 'student24', 'test1': '80', 'test2': '91',
                'test3': '86', 'test4': '99', 'test5': '96'},
            {'name': 'student28', 'test1': '90', 'test2': '100',
                'test3': '86', 'test4': '89', 'test5': '75'},
            {'name': 'student53', 'test1': '83', 'test2': '100',
                'test3': '86', 'test4': '83', 'test5': '90'},
            {'name': 'student74', 'test1': '97', 'test2': '99',
                'test3': '86', 'test4': '93', 'test5': '99'},
            {'name': 'student75', 'test1': '79', 'test2': '79',
                'test3': '86', 'test4': '78', 'test5': '68'},
            {'name': 'student78', 'test1': '88', 'test2': '98',
                'test3': '86', 'test4': '100', 'test5': '71'},
            {'name': 'student90', 'test1': '95', 'test2': '66',
                'test3': '86', 'test4': '85', 'test5': '65'},
            {'name': 'student10', 'test1': '98', 'test2': '68',
                'test3': '87', 'test4': '85', 'test5': '96'},
            {'name': 'student27', 'test1': '94', 'test2': '99',
                'test3': '87', 'test4': '91', 'test5': '86'},
            {'name': 'student42', 'test1': '72', 'test2': '86',
                'test3': '87', 'test4': '98', 'test5': '73'},
            {'name': 'student49', 'test1': '81', 'test2': '98',
                'test3': '87', 'test4': '81', 'test5': '79'},
            {'name': 'student84', 'test1': '70', 'test2': '66',
                'test3': '87', 'test4': '100', 'test5': '97'},
            {'name': 'student33', 'test1': '95', 'test2': '67',
                'test3': '88', 'test4': '81', 'test5': '97'},
            {'name': 'student38', 'test1': '68', 'test2': '98',
                'test3': '88', 'test4': '84', 'test5': '72'},
            {'name': 'student45', 'test1': '91', 'test2': '81',
                'test3': '88', 'test4': '95', 'test5': '69'},
            {'name': 'student64', 'test1': '89', 'test2': '78',
                'test3': '88', 'test4': '86', 'test5': '95'},
            {'name': 'student86', 'test1': '81', 'test2': '71',
                'test3': '88', 'test4': '98', 'test5': '81'},
            {'name': 'student76', 'test1': '80', 'test2': '72',
                'test3': '89', 'test4': '88', 'test5': '89'},
            {'name': 'student77', 'test1': '84', 'test2': '99',
                'test3': '89', 'test4': '69', 'test5': '66'},
            {'name': 'student92', 'test1': '88', 'test2': '91',
                'test3': '89', 'test4': '97', 'test5': '99'},
            {'name': 'student3', 'test1': '94', 'test2': '67',
                'test3': '90', 'test4': '95', 'test5': '84'},
            {'name': 'student40', 'test1': '94', 'test2': '97',
                'test3': '90', 'test4': '95', 'test5': '84'},
            {'name': 'student11', 'test1': '92', 'test2': '81',
                'test3': '91', 'test4': '96', 'test5': '78'},
            {'name': 'student57', 'test1': '87', 'test2': '84',
                'test3': '91', 'test4': '83', 'test5': '80'},
            {'name': 'student87', 'test1': '88', 'test2': '100',
                'test3': '91', 'test4': '75', 'test5': '66'},
            {'name': 'student44', 'test1': '67', 'test2': '100',
                'test3': '92', 'test4': '87', 'test5': '80'},
            {'name': 'student68', 'test1': '78', 'test2': '99',
                'test3': '92', 'test4': '74', 'test5': '89'},
            {'name': 'student89', 'test1': '82', 'test2': '78',
                'test3': '92', 'test4': '90', 'test5': '99'},
            {'name': 'student97', 'test1': '87', 'test2': '82',
                'test3': '92', 'test4': '88', 'test5': '92'},
            {'name': 'student8', 'test1': '88', 'test2': '71',
                'test3': '93', 'test4': '71', 'test5': '86'},
            {'name': 'student59', 'test1': '78', 'test2': '76',
                'test3': '94', 'test4': '65', 'test5': '80'},
            {'name': 'student60', 'test1': '67', 'test2': '76',
                'test3': '94', 'test4': '67', 'test5': '74'},
            {'name': 'student15', 'test1': '84', 'test2': '71',
                'test3': '95', 'test4': '77', 'test5': '77'},
            {'name': 'student29', 'test1': '89', 'test2': '93',
                'test3': '95', 'test4': '78', 'test5': '82'},
            {'name': 'student67', 'test1': '74', 'test2': '80',
                'test3': '95', 'test4': '85', 'test5': '94'},
            {'name': 'student94', 'test1': '80', 'test2': '71',
                'test3': '95', 'test4': '76', 'test5': '68'},
            {'name': 'student32', 'test1': '91', 'test2': '76',
                'test3': '96', 'test4': '73', 'test5': '91'},
            {'name': 'student51', 'test1': '94', 'test2': '93',
                'test3': '96', 'test4': '96', 'test5': '76'},
            {'name': 'student73', 'test1': '92', 'test2': '89',
                'test3': '96', 'test4': '83', 'test5': '79'},
            {'name': 'student99', 'test1': '69', 'test2': '74',
                'test3': '96', 'test4': '97', 'test5': '71'},
            {'name': 'student39', 'test1': '75', 'test2': '90',
                'test3': '97', 'test4': '86', 'test5': '72'},
            {'name': 'student56', 'test1': '98', 'test2': '80',
                'test3': '97', 'test4': '68', 'test5': '91'},
            {'name': 'student4', 'test1': '68', 'test2': '85',
                'test3': '98', 'test4': '69', 'test5': '77'},
            {'name': 'student30', 'test1': '66', 'test2': '92',
                'test3': '98', 'test4': '92', 'test5': '100'},
            {'name': 'student41', 'test1': '71', 'test2': '77',
                'test3': '98', 'test4': '95', 'test5': '70'},
            {'name': 'student54', 'test1': '92', 'test2': '72',
                'test3': '98', 'test4': '70', 'test5': '98'},
            {'name': 'student71', 'test1': '95', 'test2': '98',
                'test3': '98', 'test4': '98', 'test5': '75'},
            {'name': 'student95', 'test1': '78', 'test2': '71',
                'test3': '98', 'test4': '78', 'test5': '96'},
            {'name': 'student6', 'test1': '72', 'test2': '97',
                'test3': '99', 'test4': '69', 'test5': '83'},
            {'name': 'student9', 'test1': '79', 'test2': '69',
                'test3': '99', 'test4': '73', 'test5': '76'},
            {'name': 'student7', 'test1': '66', 'test2': '99',
                'test3': '100', 'test4': '96', 'test5': '81'},
            {'name': 'student36', 'test1': '76', 'test2': '69',
                'test3': '100', 'test4': '97', 'test5': '83'},
            {'name': 'student48', 'test1': '98', 'test2': '69',
                'test3': '100', 'test4': '84', 'test5': '80'},
            {'name': 'student65', 'test1': '80', 'test2': '75',
                'test3': '100', 'test4': '83', 'test5': '77'}
        ]
        self.assertEqual(expected_value, output)

    @weight(3)
    @visibility('visible')
    @number("eas503_ex51_02")
    def test_eas503_ex51_02(self):
        import types
        l_func, output = self.assignment.eas503_ex51('grades_dict.json')
        self.assertEqual(types.LambdaType, type(l_func))

    @weight(3)
    @visibility('visible')
    @number("eas503_ex51_03")
    def test_eas503_ex51_03(self):
        import types
        l_func, output = self.assignment.eas503_ex51('grades_dict.json')
        lines = [{
            "name": "student19",
            "test1": "70",
            "test2": "70",
            "test3": "83",
            "test4": "99",
            "test5": "97"
        },
            {
            "name": "student20",
            "test1": "68",
            "test2": "68",
            "test3": "81",
            "test4": "74",
            "test5": "76"
        },
            {
            "name": "student21",
            "test1": "74",
            "test2": "73",
            "test3": "84",
            "test4": "84",
            "test5": "69"
        },
            {
            "name": "student22",
            "test1": "65",
            "test2": "87",
            "test3": "85",
            "test4": "78",
            "test5": "98"
        },
            {
            "name": "student23",
            "test1": "88",
            "test2": "95",
            "test3": "85",
            "test4": "67",
            "test5": "93"
        },
            {
            "name": "student24",
            "test1": "80",
            "test2": "91",
            "test3": "86",
            "test4": "99",
            "test5": "96"
        },
            {
            "name": "student25",
            "test1": "77",
            "test2": "86",
            "test3": "79",
            "test4": "70",
            "test5": "92"
        },
            {
            "name": "student26",
            "test1": "80",
            "test2": "78",
            "test3": "75",
            "test4": "69",
            "test5": "87"
        }, ]

        expected_value = [{'name': 'student26', 'test1': '80', 'test2': '78', 'test3': '75', 'test4': '69', 'test5': '87'},
                          {'name': 'student25', 'test1': '77', 'test2': '86',
                              'test3': '79', 'test4': '70', 'test5': '92'},
                          {'name': 'student20', 'test1': '68', 'test2': '68',
                              'test3': '81', 'test4': '74', 'test5': '76'},
                          {'name': 'student19', 'test1': '70', 'test2': '70',
                           'test3': '83', 'test4': '99', 'test5': '97'},
                          {'name': 'student21', 'test1': '74', 'test2': '73',
                           'test3': '84', 'test4': '84', 'test5': '69'},
                          {'name': 'student22', 'test1': '65', 'test2': '87',
                           'test3': '85', 'test4': '78', 'test5': '98'},
                          {'name': 'student23', 'test1': '88', 'test2': '95',
                           'test3': '85', 'test4': '67', 'test5': '93'},
                          {'name': 'student24', 'test1': '80', 'test2': '91', 'test3': '86', 'test4': '99', 'test5': '96'}]

        self.assertEqual(expected_value, sorted(lines, key=l_func))

    @weight(3)
    @visibility('visible')
    @number("eas503_ex52_1")
    def test_eas503_ex52_1(self):
        value = self.assignment.eas503_ex52(range(1, 20))
        self.assertEqual([3, 4, 6, 8, 9, 12, 15, 16, 18], value)

    @weight(3)
    @visibility('visible')
    @number("eas503_ex52_2")
    def test_eas503_ex52_2(self):
        value = self.assignment.eas503_ex52(range(101, 140))
        self.assertEqual([
            102,
            104,
            105,
            108,
            111,
            112,
            114,
            116,
            117,
            120,
            123,
            124,
            126,
            128,
            129,
            132,
            135,
            136,
            138], value)

    @weight(3)
    @visibility('visible')
    @number("eas503_ex53_1")
    def test_eas503_ex53_1(self):
        value = self.assignment.eas503_ex53(range(20))
        expected_value = [
            0, 5, 6, 15, 12,
            25, 18, 35, 24, 45,
            30, 55, 36, 65, 42,
            75, 48, 85, 54, 95
        ]
        self.assertEqual(expected_value, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_ex53_2")
    def test_eas503_ex53_2(self):
        value = self.assignment.eas503_ex53(range(200, 220))
        expected_value = [
            600, 1005, 606, 1015,
            612, 1025, 618, 1035,
            624, 1045, 630, 1055,
            636, 1065, 642, 1075, 648, 1085, 654, 1095]

        self.assertEqual(expected_value, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_ex54_1")
    def test_eas503_ex54_1(self):
        input_dict = {
            'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31,
        }
        value = self.assignment.eas503_ex54(input_dict, 31)
        expected_value = ['January', 'March', 'May',
                          'July', 'August', 'October', 'December']
        self.assertEqual(expected_value, value)

    @weight(3)
    @visibility('visible')
    @number("eas503_ex54_2")
    def test_eas503_ex54_2(self):
        input_dict = {
            'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31,
        }
        value = self.assignment.eas503_ex54(input_dict, 30)
        expected_value = ['April', 'June', 'September', 'November']
        self.assertEqual(expected_value, value)

