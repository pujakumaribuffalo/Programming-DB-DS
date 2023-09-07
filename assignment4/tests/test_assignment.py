import unittest
import assignment
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestAssignment(unittest.TestCase):
    def setUp(self):
        self.assignment = assignment

    @weight(3)
    @visibility('visible')
    @number("1.1")
    def test_IteratorClass_1(self):
        self.assertRaises(ValueError, assignment.IteratorClass,
                          range(5, 10), [1, 2, 3], 'div')

    @weight(3)
    @visibility('visible')
    @number("1.2")
    def test_IteratorClass_2(self):
        self.assertRaises(ValueError, assignment.IteratorClass, [
                          1, 2, 3], range(5, 10), 'div')

    @weight(3)
    @visibility('visible')
    @number("1.3")
    def test_IteratorClass_3(self):
        self.assertRaises(ValueError, assignment.IteratorClass, [
                          1, 2, 3], [1, 2, 3], 'abc')

    @weight(3)
    @visibility('visible')
    @number("1.4")
    def test_IteratorClass_4(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        add_iterator = assignment.IteratorClass(x, y, 'add')
        self.assertEqual([ele for ele in add_iterator], [55, 57, 59, 61, 63])

    @weight(3)
    @visibility('visible')
    @number("1.5")
    def test_IteratorClass_5(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        sub_iterator = assignment.IteratorClass(x, y, 'sub')
        self.assertEqual([ele for ele in sub_iterator],
                         [-45, -45, -45, -45, -45])

    @weight(3)
    @visibility('visible')
    @number("1.6")
    def test_IteratorClass_6(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        mul_iterator = assignment.IteratorClass(x, y, 'mul')
        self.assertEqual([ele for ele in mul_iterator],
                         [250, 306, 364, 424, 486])

    @weight(3)
    @visibility('visible')
    @number("1.7")
    def test_IteratorClass_7(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        div_iterator = assignment.IteratorClass(x, y, 'div')
        self.assertEqual([ele for ele in div_iterator],
                         [0.1, 0.12, 0.13, 0.15, 0.17])

    @weight(3)
    @visibility('visible')
    @number("1.8")
    def test_IteratorClass_8(self):
        x = list(range(5, 10))
        y = list(range(50, 55))
        div_iterator = assignment.IteratorClass(x, y, 'div')
        self.assertEqual(hasattr(div_iterator.__class__, '__next__'), True)

    @weight(3)
    @visibility('visible')
    @number("2.1")
    def test_ListV2_1(self):
        self.assertRaises(ValueError, assignment.ListV2,  3)

    @weight(3)
    @visibility('visible')
    @number("2.2")
    def test_ListV2_2(self):
        self.assertRaises(ValueError, assignment.ListV2,  '3')

    @weight(3)
    @visibility('visible')
    @number("2.3")
    def test_ListV2_3(self):
        self.assertRaises(ValueError, assignment.ListV2,  3.14)

    @weight(3)
    @visibility('visible')
    @number("2.4")
    def test_ListV2_4(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        l2 = assignment.ListV2(list(range(50, 55)))
        result = l1 + l2
        self.assertEqual(type(result),  assignment.ListV2)

    @weight(3)
    @visibility('visible')
    @number("2.5")
    def test_ListV2_5(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        l2 = assignment.ListV2(list(range(50, 55)))
        result = l1 + l2
        self.assertEqual([ele for ele in result],  [55, 57, 59, 61, 63])

    @weight(3)
    @visibility('visible')
    @number("2.6")
    def test_ListV2_6(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        l2 = assignment.ListV2(list(range(50, 55)))
        result = l1 - l2
        self.assertEqual([ele for ele in result],  [-45, -45, -45, -45, -45])

    @weight(3)
    @visibility('visible')
    @number("2.7")
    def test_ListV2_7(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        l2 = assignment.ListV2(list(range(50, 55)))
        result = l1 * l2
        self.assertEqual([ele for ele in result],  [250, 306, 364, 424, 486])

    @weight(3)
    @visibility('visible')
    @number("2.8")
    def test_ListV2_8(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        l2 = assignment.ListV2(list(range(50, 55)))
        result = l1 / l2
        self.assertEqual([ele for ele in result],  [
                         0.1, 0.12, 0.13, 0.15, 0.17])

    @weight(3)
    @visibility('visible')
    @number("2.9")
    def test_ListV2_9(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        result = l1 + 5
        self.assertEqual([ele for ele in result],  [10, 11, 12, 13, 14])

    @weight(3)
    @visibility('visible')
    @number("2.10")
    def test_ListV2_10(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        result = l1 - 5
        self.assertEqual([ele for ele in result],  [0, 1, 2, 3, 4])

    @weight(3)
    @visibility('visible')
    @number("2.11")
    def test_ListV2_11(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        result = l1 * 5
        self.assertEqual([ele for ele in result],  [25, 30, 35, 40, 45])

    @weight(3)
    @visibility('visible')
    @number("2.12")
    def test_ListV2_12(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        result = l1 / 5
        self.assertEqual([ele for ele in result],  [1.0, 1.2, 1.4, 1.6, 1.8])

    @weight(3)
    @visibility('visible')
    @number("2.13")
    def test_ListV2_13(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        l2 = list(range(50, 55))
        result = l1 + l2
        self.assertEqual([ele for ele in result],  [55, 57, 59, 61, 63])

    @weight(3)
    @visibility('visible')
    @number("2.14")
    def test_ListV2_14(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        l2 = list(range(50, 55))
        result = l1 - l2
        self.assertEqual([ele for ele in result],  [-45, -45, -45, -45, -45])

    @weight(3)
    @visibility('visible')
    @number("2.15")
    def test_ListV2_15(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        l2 = tuple(range(50, 55))
        result = l1 * l2
        self.assertEqual([ele for ele in result],  [250, 306, 364, 424, 486])

    @weight(3)
    @visibility('visible')
    @number("2.16")
    def test_ListV2_16(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        l2 = tuple(range(50, 55))
        result = l1 / l2
        self.assertEqual([ele for ele in result],  [0.1, 0.12, 0.13, 0.15, 0.17])

    @weight(3)
    @visibility('visible')
    @number("2.17")
    def test_ListV2_17(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        self.assertEqual(l1.__repr__(),  '[5, 6, 7, 8, 9]')

    @weight(3)
    @visibility('visible')
    @number("2.18")
    def test_ListV2_18(self):
        l1 = assignment.ListV2(list(range(5, 10)))
        self.assertEqual(hasattr(l1.__class__, '__next__'), True)


    @weight(4)
    @visibility('visible')
    @number("3.1")
    def test_Pound_01(self):
        p1 = assignment.Pound(13, 15)
        p2 = assignment.Pound(3, 5)
        p3 = p1 + p2
        self.assertEqual(p3.__repr__(), "Pound(17, 4)")
        self.assertEqual(p3.__str__(), "17 lb 4 oz")
    
    @weight(4)
    @visibility('visible')
    @number("3.2")
    def test_Pound_02(self):
        p1 = assignment.Pound(12, 0)
        p2 = assignment.Pound(3, 5)
        p3 = p1 + p2
        self.assertEqual(p3.__repr__(), "Pound(15, 5)")
        self.assertEqual(p3.__str__(), "15 lb 5 oz")


    @weight(4)
    @visibility('visible')
    @number("3.3")
    def test_Pound_03(self):
        p1 = assignment.Pound(15, 15)
        p2 = assignment.Pound(13, 14)
        p3 = p1 + p2
        self.assertEqual(p3.__repr__(), "Pound(29, 13)")
        self.assertEqual(p3.__str__(), "29 lb 13 oz")
    
    @weight(4)
    @visibility('visible')
    @number("3.4")
    def test_Pound_04(self):
        p1 = assignment.Pound(5, 7)
        p2 = assignment.Pound(3, 9)
        p3 = p1 - p2
        self.assertEqual(p3.__repr__(), "Pound(1, 14)")
        self.assertEqual(p3.__str__(), "1 lb 14 oz")

    @weight(4)
    @visibility('visible')
    @number("3.5")
    def test_Pound_05(self):
        p1 = assignment.Pound(15, 0)
        p2 = assignment.Pound(4, 9)
        p3 = p1 - p2
        self.assertEqual(p3.__repr__(), "Pound(10, 7)")
        self.assertEqual(p3.__str__(), "10 lb 7 oz")
    
    @weight(4)
    @visibility('visible')
    @number("3.6")
    def test_Pound_06(self):
        p1 = assignment.Pound(13, 8)
        p2 = assignment.Pound(14, 15)       
        with self.assertRaises(ValueError):
            p3 = p1 - p2
