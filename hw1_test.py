from data import *
from hw1 import *
import unittest


# Write your test cases for each part below.
# All intermediate variables will follow format of Part#_Case#, EX: two_three = Part 2 Case 3
class TestCases(unittest.TestCase):
    # Part 1
    def test_one_vowel(self):
        word = "abc"
        self.assertEqual(vowel_count(word), 1)

    def test_no_vowel(self):
        word = "bc"
        self.assertEqual(vowel_count(word), 0)

    def test_upper_vowel(self):
        word = "Abc"
        self.assertEqual(vowel_count(word), 1)

    def test_upper_lower_vowel(self):
        word = "Abce"
        self.assertEqual(vowel_count(word), 2)

    # Part 2
    def test_multi_list(self):
        list = [[2, 4], [5, 6, 7, 8], [1], [-2, 12], [0, 0]]
        self.assertEqual(short_lists(list),[[2,4],[-2,12],[0,0]])

    def test_odd_list(self):
        list = [[0],[1,2,3]]
        self.assertEqual(short_lists(list), [])

    def test_empty_list(self):
        list = []
        self.assertEqual(short_lists(list), [])

    # Part 3
    def test_multi_ascending_list(self):
        list = [[2, 2], [1], [18, 9, 12], [1, 5], [8, 5]]
        self.assertEqual(ascending_pairs(list), [[2,2],[1],[18,9,12],[1,5],[5,8]])

    def test_empty_ascending_list(self):
        list = []
        self.assertEqual(ascending_pairs(list), [])

    def test_simple_ascending_list(self):
        list = [[4,3],[3,4]]
        self.assertEqual(ascending_pairs(list), [[3,4],[3,4]])

    # Part 4
    def test_price_dollar_plus(self):
        p1=Price(5,80)
        p2=Price(3,50)
        self.assertEqual(add_prices(p1,p2),Price(9,30))
    def test_price_dollar_even(self):
        p1=Price(3,50)
        p2=Price(1,50)
        self.assertEqual(add_prices(p1,p2),Price(5,0))
    def test_price_dollar_short(self):
        p1=Price(1,49)
        p2=Price(1,50)
        self.assertEqual(add_prices(p1,p2),Price(2,99))
    def test_price_dollar_perfect(self):
        p1=Price(1,0)
        p2=Price(0,100)
        self.assertEqual(add_prices(p1,p2),Price(2,0))

    # Part 5
    def test_rectangle_positive(self):
        top_left = Point(1, 4)
        bottom_right = Point(5, 1)
        rect = Rectangle(top_left, bottom_right)
        self.assertEqual(rectangle_area(rect), 12)
    def test_rectangle_mixed(self):
        top_left = Point(-1, 4)
        bottom_right = Point(5, -1)
        rect = Rectangle(top_left, bottom_right)
        self.assertEqual(rectangle_area(rect), 30)
    def test_rectangle_negatives(self):
        top_left = Point(-6, -1)
        bottom_right = Point(-2, -6)
        rect = Rectangle(top_left, bottom_right)
        self.assertEqual(rectangle_area(rect), 20)

    # Part 6
    def test_book_A(self):
        book1 = Book(['Author A', 'Author B'], 'Book 1')
        book2 = Book(['Author A'], 'Book 2')
        book3 = Book(['Author C'], 'Book 3')
        books_list = [book1, book2, book3]
        self.assertEqual(books_by_author('Author A', books_list), [Book(['Author A', 'Author B'], 'Book 1'), Book(['Author A'], 'Book 2')])

    def test_book_B(self):
        book1 = Book(['Author A'], 'Book 1')
        book2 = Book(['Author A'], 'Book 2')
        book3 = Book(['Author B'], 'Book 3')
        book4 = Book(['Author A'], 'Book 4')
        book5 = Book(['Author B'], 'Book 5')
        books_list = [book1, book2, book3, book4, book5]
        self.assertEqual(books_by_author('Author B', books_list), [Book(['Author B'], 'Book 3'), Book(['Author B'], 'Book 5')])



    # Part 7
    def test_smallest_encircle_positive(self):
        top_left = Point(0, 10)
        bottom_right = Point(10, 0)
        rect = Rectangle(top_left, bottom_right)
        self.assertEqual(circle_bound(rect),Circle(Point(5.0, 5.0), 7.0710678118654755))

    def test_smallest_encircle_mixed(self):
        top_left = Point(-2, 4)
        bottom_right = Point(8, -3)
        rect = Rectangle(top_left, bottom_right)
        self .assertEqual(circle_bound(rect),Circle(Point(3,.5),6.103277807866851))

    # Part 8
    def test_employee_pay_given(self):
        employees = [
            Employee("Alice", 3000),
            Employee("Bob", 2500),
            Employee("Charlie", 4000),
            Employee("Dana", 2000)
        ]
        self.assertEqual(below_pay_average(employees), ['Bob','Dana'])

    def test_employee_pay_empty(self):
        employees = []
        self.assertEqual(below_pay_average(employees), [])




if __name__ == '__main__':
    unittest.main()
