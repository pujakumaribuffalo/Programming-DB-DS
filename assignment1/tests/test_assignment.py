import unittest

import assignment
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestAssignment1(unittest.TestCase):
    def setUp(self):
        self.assignment = assignment

    @weight(3)
    @visibility('visible')
    @number("01.1")
    def test_ex01_1(self):
        value = self.assignment.eas503_ex1('Brian')
        self.assertEqual('Hello, Brian, nice to meet you!', value)

    @weight(3)
    @visibility('visible')
    @number("01.2")
    def test_ex01_2(self):
        value = self.assignment.eas503_ex1('John')
        self.assertEqual('Hello, John, nice to meet you!', value)

    @weight(3)
    @visibility('visible')
    @number("01.3")
    def test_ex01_3(self):
        value = self.assignment.eas503_ex1('Jane')
        self.assertEqual('Hello, Jane, nice to meet you!', value)

    @weight(3)
    @visibility('visible')
    @number("02.1")
    def test_ex02_1(self):
        value = self.assignment.eas503_ex2(1, 2, 3)
        self.assertEqual(
            'The value of x is: 1.\nThe value of y is: 2.\nThe value of z is: 3.', value)

    @weight(3)
    @visibility('visible')
    @number("02.2")
    def test_ex02_2(self):
        value = self.assignment.eas503_ex2(40, 50, 60)
        self.assertEqual(
            'The value of x is: 40.\nThe value of y is: 50.\nThe value of z is: 60.', value)

    @weight(3)
    @visibility('visible')
    @number("03.1")
    def test_ex03_1(self):
        value = self.assignment.eas503_ex3(45.23, 89.34)
        self.assertEqual(
            'The area of a rectangle with length 45.23 and width 89.34 is 4040.85.', value)

    @weight(3)
    @visibility('visible')
    @number("03.2")
    def test_ex03_2(self):
        value = self.assignment.eas503_ex3(40.90, 50.55)
        self.assertEqual(
            'The area of a rectangle with length 40.9 and width 50.55 is 2067.49.', value)

    @weight(3)
    @visibility('visible')
    @number("04.1")
    def test_ex04_1(self):
        value = self.assignment.eas503_ex4(15)
        self.assertEqual(2827.43, value)

    @weight(3)
    @visibility('visible')
    @number("04.2")
    def test_ex04_2(self):
        value = self.assignment.eas503_ex4(7.25)
        self.assertEqual(660.52, value)

    @weight(3)
    @visibility('visible')
    @number("04.3")
    def test_ex04_3(self):
        value = self.assignment.eas503_ex4(5.25)
        self.assertEqual(346.36, value)

    @weight(3)
    @visibility('visible')
    @number("04.4")
    def test_ex04_4(self):
        value = self.assignment.eas503_ex4(17.25)
        self.assertEqual(3739.28, value)

    @weight(3)
    @visibility('visible')
    @number("05.1")
    def test_ex05_1(self):
        value = self.assignment.eas503_ex5(15)
        self.assertEqual(14137.17, value)

    @weight(3)
    @visibility('visible')
    @number("05.2")
    def test_ex05_2(self):
        value = self.assignment.eas503_ex5(7.5)
        self.assertEqual(1767.15, value)

    @weight(3)
    @visibility('visible')
    @number("05.3")
    def test_ex05_3(self):
        value = self.assignment.eas503_ex5(78.2)
        self.assertEqual(2003128.77, value)

    @weight(3)
    @visibility('visible')
    @number("05.4")
    def test_ex05_4(self):
        value = self.assignment.eas503_ex5(8.2)
        self.assertEqual(2309.56, value)

    @weight(3)
    @visibility('visible')
    @number("06.1")
    def test_ex06_1(self):
        value = self.assignment.eas503_ex6(150, 65)
        self.assertEqual(24.96, value)

    @weight(3)
    @visibility('visible')
    @number("06.2")
    def test_ex06_2(self):
        value = self.assignment.eas503_ex6(110, 55)
        self.assertEqual(25.56, value)

    @weight(3)
    @visibility('visible')
    @number("07.1")
    def test_ex07_1(self):
        value = self.assignment.eas503_ex7(20, 50)
        self.assertEqual('The refund amount is $14.50.', value)

    @weight(3)
    @visibility('visible')
    @number("07.2")
    def test_ex07_2(self):
        value = self.assignment.eas503_ex7(67, 59)
        self.assertEqual('The refund amount is $21.45.', value)

    @weight(3)
    @visibility('visible')
    @number("08.1")
    def test_ex08_1(self):
        value = self.assignment.eas503_ex8(10, 5)
        expected_result = """The sum of 10 and 5 is 15.
The difference when 5 is subtracted from 10 is 5.
The product of 10 and 5 is 50.
The quotient when 10 is divided by 5 is 2.
The remainder when 10 is divided by 5 is 0.
The result of 10^5 is 100000."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("08.2")
    def test_ex08_2(self):
        value = self.assignment.eas503_ex8(6, 5)
        expected_result = """The sum of 6 and 5 is 11.
The difference when 5 is subtracted from 6 is 1.
The product of 6 and 5 is 30.
The quotient when 6 is divided by 5 is 1.
The remainder when 6 is divided by 5 is 1.
The result of 6^5 is 7776."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("09.1")
    def test_ex09_1(self):
        value = self.assignment.eas503_ex9(1500, 4.3, 4)
        self.assertEqual(
            'After 4 years at 4.3%, the investment will be worth $1758.00.', value)

    @weight(3)
    @visibility('visible')
    @number("09.2")
    def test_ex09_2(self):
        value = self.assignment.eas503_ex9(150000, 6.5, 30)
        self.assertEqual(
            'After 30 years at 6.5%, the investment will be worth $442500.00.', value)

    @weight(3)
    @visibility('visible')
    @number("10.1")
    def test_ex10_1(self):
        value = self.assignment.eas503_ex10(1500, 4.3, 6, 4)
        self.assertEqual(
            '$1500 invested at 4.3% for 6 years compounded 4 times per year is $1938.84.', value)

    @weight(3)
    @visibility('visible')
    @number("10.2")
    def test_ex10_2(self):
        value = self.assignment.eas503_ex10(150000, 6.5, 30, 12)
        self.assertEqual(
            '$150000 invested at 6.5% for 30 years compounded 12 times per year is $1048769.70.', value)

    @weight(3)
    @visibility('visible')
    @number("11.1")
    def test_ex11_1(self):
        value = self.assignment.eas503_ex11('Buffalo')
        self.assertEqual("The input string 'Buffalo' has 7 characters.", value)

    @weight(3)
    @visibility('visible')
    @number("11.2")
    def test_ex11_2(self):
        value = self.assignment.eas503_ex11('University at Buffalo')
        self.assertEqual(
            "The input string 'University at Buffalo' has 21 characters.", value)

    @weight(3)
    @visibility('visible')
    @number("11.3")
    def test_ex11_3(self):
        value = self.assignment.eas503_ex11(
            'Center for Computational Research (CCR)')
        self.assertEqual(
            "The input string 'Center for Computational Research (CCR)' has 39 characters.", value)

    @weight(3)
    @visibility('visible')
    @number("12.1")
    def test_ex12_1(self):
        value = self.assignment.eas503_ex12('dog', 'walk', 'blue', 'quickly')
        self.assertEqual(
            "Do you walk your blue dog quickly? That's hilarious!", value)

    @weight(3)
    @visibility('visible')
    @number("12.2")
    def test_ex12_2(self):
        value = self.assignment.eas503_ex12('cat', 'walk', 'brown', 'slowly')
        self.assertEqual(
            "Do you walk your brown cat slowly? That's hilarious!", value)

    @weight(3)
    @visibility('visible')
    @number("13.1")
    def test_ex13_1(self):
        value = self.assignment.eas503_ex13(25, 65, 2015)
        expected_result = """Your current age is: 25.
You would like to retire at: 65.
You have 40 years left until you can retire.
It's 2015, so you can retire in 2055."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("13.2")
    def test_ex13_2(self):
        value = self.assignment.eas503_ex13(36, 72, 2021)
        expected_result = """Your current age is: 36.
You would like to retire at: 72.
You have 36 years left until you can retire.
It's 2021, so you can retire in 2057."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("14.1")
    def test_ex14_1(self):
        value = self.assignment.eas503_ex14(15, 20)
        expected_result = """The length of the room in feet is 15.
The width of the room in feet is 20.
The dimension of the room is 15 by 20 feet.
The area is
300 square feet
27.87 square meters"""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("14.2")
    def test_ex14_2(self):
        value = self.assignment.eas503_ex14(45, 35)
        expected_result = """The length of the room in feet is 45.
The width of the room in feet is 35.
The dimension of the room is 45 by 35 feet.
The area is
1575 square feet
146.32 square meters"""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("15.1")
    def test_ex15_1(self):
        value = self.assignment.eas503_ex15(8, 2)
        expected_result = """There are 8 people with 2 pizzas.
Each person gets 2 pieces of pizza.
There are 0 leftover pieces."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("15.2")
    def test_ex15_2(self):
        value = self.assignment.eas503_ex15(20, 6)
        expected_result = """There are 20 people with 6 pizzas.
Each person gets 2 pieces of pizza.
There are 8 leftover pieces."""
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("16.1")
    def test_ex16_1(self):
        value = self.assignment.eas503_ex16(12, 30)
        expected_result = 'You will need to purchase 2 gallons of paint to cover 360 square feet.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("16.2")
    def test_ex16_2(self):
        value = self.assignment.eas503_ex16(25, 35)
        expected_result = 'You will need to purchase 3 gallons of paint to cover 875 square feet.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("17.1")
    def test_ex17_1(self):
        value = self.assignment.eas503_ex17(3.14159)
        expected_result = 'The value is: 3.1416.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("17.2")
    def test_ex17_2(self):
        value = self.assignment.eas503_ex17(1.61803398875)
        expected_result = 'The value is: 1.6180.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("18.1")
    def test_ex18_1(self):
        value = self.assignment.eas503_ex18(3.14159)
        expected_result = 'The value is:     3.1416.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("18.2")
    def test_ex18_2(self):
        value = self.assignment.eas503_ex18(1.61803398875)
        expected_result = 'The value is:     1.6180.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("19.1")
    def test_ex19_1(self):
        value = self.assignment.eas503_ex19(3.14159)
        expected_result = 'The value is: 3.141590--.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("19.2")
    def test_ex19_2(self):
        value = self.assignment.eas503_ex19(1.61803398875)
        expected_result = 'The value is: 1.618034--.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("20.1")
    def test_ex20_1(self):
        value = self.assignment.eas503_ex20(3.14159)
        expected_result = 'The value is: --3.141590--.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("20.2")
    def test_ex20_2(self):
        value = self.assignment.eas503_ex20(1.61803398875)
        expected_result = 'The value is: --1.618034--.'
        self.assertEqual(expected_result, value)

    @weight(3)
    @visibility('visible')
    @number("21.1")
    def test_ex21_1(self):
        value = self.assignment.eas503_ex21(40, 25)
        self.assertEqual(1000, value)

    @weight(3)
    @visibility('visible')
    @number("21.2")
    def test_ex21_2(self):
        value = self.assignment.eas503_ex21(65, 63.4)
        self.assertEqual(4913.5, value)

    @weight(3)
    @visibility('visible')
    @number("21.3")
    def test_ex21_3(self):
        value = self.assignment.eas503_ex21(20, 45)
        self.assertEqual(900, value)

    @weight(3)
    @visibility('visible')
    @number("21.4")
    def test_ex21_4(self):
        value = self.assignment.eas503_ex21(55, 35.5)
        self.assertEqual(2218.75, value)

    @weight(3)
    @visibility('visible')
    @number("22.1")
    def test_ex22_1(self):
        value = self.assignment.eas503_ex22(0)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("22.2")
    def test_ex22_2(self):
        value = self.assignment.eas503_ex22(1)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("22.3")
    def test_ex22_3(self):
        value = self.assignment.eas503_ex22(2)
        self.assertEqual('D', value)

    @weight(3)
    @visibility('visible')
    @number("22.4")
    def test_ex22_4(self):
        value = self.assignment.eas503_ex22(3)
        self.assertEqual('C', value)

    @weight(3)
    @visibility('visible')
    @number("22.5")
    def test_ex22_5(self):
        value = self.assignment.eas503_ex22(4)
        self.assertEqual('B', value)

    @weight(3)
    @visibility('visible')
    @number("22.6")
    def test_ex22_6(self):
        value = self.assignment.eas503_ex22(5)
        self.assertEqual('A', value)

    @weight(3)
    @visibility('visible')
    @number("23.1")
    def test_ex23_1(self):
        value = self.assignment.eas503_ex23(55)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("23.2")
    def test_ex23_2(self):
        value = self.assignment.eas503_ex23(35)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("23.3")
    def test_ex23_3(self):
        value = self.assignment.eas503_ex23(65)
        self.assertEqual('D', value)

    @weight(3)
    @visibility('visible')
    @number("23.4")
    def test_ex23_4(self):
        value = self.assignment.eas503_ex23(73)
        self.assertEqual('C', value)

    @weight(3)
    @visibility('visible')
    @number("23.5")
    def test_ex23_5(self):
        value = self.assignment.eas503_ex23(87)
        self.assertEqual('B', value)

    @weight(3)
    @visibility('visible')
    @number("23.6")
    def test_ex23_6(self):
        value = self.assignment.eas503_ex23(92)
        self.assertEqual('A', value)

    @weight(3)
    @visibility('visible')
    @number("23.7")
    def test_ex23_7(self):
        value = self.assignment.eas503_ex23(45)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("23.8")
    def test_ex23_8(self):
        value = self.assignment.eas503_ex23(25)
        self.assertEqual('F', value)

    @weight(3)
    @visibility('visible')
    @number("23.9")
    def test_ex23_9(self):
        value = self.assignment.eas503_ex23(68)
        self.assertEqual('D', value)

    @weight(3)
    @visibility('visible')
    @number("23.10")
    def test_ex23_10(self):
        value = self.assignment.eas503_ex23(77)
        self.assertEqual('C', value)

    @weight(3)
    @visibility('visible')
    @number("23.11")
    def test_ex23_11(self):
        value = self.assignment.eas503_ex23(83)
        self.assertEqual('B', value)

    @weight(3)
    @visibility('visible')
    @number("23.12")
    def test_ex23_12(self):
        value = self.assignment.eas503_ex23(96)
        self.assertEqual('A', value)

    @weight(3)
    @visibility('visible')
    @number("24.1")
    def test_ex24_1(self):
        value = self.assignment.eas503_ex24(6)
        self.assertEqual('Freshman', value)

    @weight(3)
    @visibility('visible')
    @number("24.2")
    def test_ex24_2(self):
        value = self.assignment.eas503_ex24(13)
        self.assertEqual('Sophomore', value)

    @weight(3)
    @visibility('visible')
    @number("24.3")
    def test_ex24_3(self):
        value = self.assignment.eas503_ex24(23)
        self.assertEqual('Junior', value)

    @weight(3)
    @visibility('visible')
    @number("24.4")
    def test_ex24_4(self):
        value = self.assignment.eas503_ex24(45)
        self.assertEqual('Senior', value)

    @weight(3)
    @visibility('visible')
    @number("24.5")
    def test_ex24_5(self):
        value = self.assignment.eas503_ex24(3)
        self.assertEqual('Freshman', value)

    @weight(3)
    @visibility('visible')
    @number("24.6")
    def test_ex24_6(self):
        value = self.assignment.eas503_ex24(15)
        self.assertEqual('Sophomore', value)

    @weight(3)
    @visibility('visible')
    @number("24.7")
    def test_ex24_7(self):
        value = self.assignment.eas503_ex24(20)
        self.assertEqual('Junior', value)

    @weight(3)
    @visibility('visible')
    @number("24.8")
    def test_ex24_8(self):
        value = self.assignment.eas503_ex24(35)
        self.assertEqual('Senior', value)

    @weight(3)
    @visibility('visible')
    @number("25.1")
    def test_ex25_1(self):
        value = self.assignment.eas503_ex25(55, 85)
        self.assertEqual(200, value)

    @weight(3)
    @visibility('visible')
    @number("25.2")
    def test_ex25_2(self):
        value = self.assignment.eas503_ex25(55, 45)
        self.assertEqual('Legal', value)

    @weight(3)
    @visibility('visible')
    @number("25.3")
    def test_ex25_3(self):
        value = self.assignment.eas503_ex25(55, 100)
        self.assertEqual(475, value)

    @weight(3)
    @visibility('visible')
    @number("25.4")
    def test_ex25_4(self):
        value = self.assignment.eas503_ex25(55, 75)
        self.assertEqual(150, value)

    @weight(3)
    @visibility('visible')
    @number("25.5")
    def test_ex25_5(self):
        value = self.assignment.eas503_ex25(55, 35)
        self.assertEqual('Legal', value)

    @weight(3)
    @visibility('visible')
    @number("25.6")
    def test_ex25_6(self):
        value = self.assignment.eas503_ex25(55, 120)
        self.assertEqual(575, value)

    @weight(3)
    @visibility('visible')
    @number("26.1")
    def test_ex26_1(self):
        value = self.assignment.eas503_ex26('Kayak')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("26.2")
    def test_ex26_2(self):
        value = self.assignment.eas503_ex26('Rotator')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("26.3")
    def test_ex26_3(self):
        value = self.assignment.eas503_ex26('AACA')
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("26.4")
    def test_ex26_4(self):
        value = self.assignment.eas503_ex26('Stats')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("26.5")
    def test_ex26_5(self):
        value = self.assignment.eas503_ex26('Madam')
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("26.6")
    def test_ex26_6(self):
        value = self.assignment.eas503_ex26('Test1234')
        self.assertEqual(False, value)

    