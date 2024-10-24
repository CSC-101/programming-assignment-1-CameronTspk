from data import *
from hw1 import *
import unittest


# Write your test cases for each part below.
# All intermediate variables will follow format of Part#_Case#, EX: two_three = Part 2 Case 3
class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count(self):
        word = "abc"
        self.assertEqual(vowel_count(word), 1)

    print("Part One test results")
    One_One = vowel_count("Monsters University")
    print("Monsters University yields a vowel count of " + str(One_One))
    One_Two = vowel_count("apple")
    print("apple yields a vowel count of " + str(One_Two))
    One_Three = vowel_count("brfd")
    print("brfd yields a vowel count of " + str(One_Three))

    # Part 2
    print("Part Two test results")
    Two_One = short_lists([[2, 4], [5, 6, 7, 8], [1], [-2, 12], [0, 0]])
    print(Two_One)
    Two_Two = short_lists([[0],[1,2,3]])
    print(Two_Two)
    Two_Three = short_lists([])
    print( Two_Three)
    # Part 3
    print("Part Three test results")
    Three_One = ascending_pairs([[2, 2], [1], [18, 9, 12], [1, 5], [8, 5]])
    print(Three_One)
    Three_Two = ascending_pairs([])
    print(Three_Two)
    Three_Three = ascending_pairs([[4,3],[3,4]])
    print(Three_Three)
    Three_Four = ascending_pairs([[0],[1,2,3]])
    print(Three_Four)
    # Part 4
    print("Part Four test results")
    Four_One = add_prices(Price(5,80), Price(3,50))
    print(Four_One)
    Four_Two = add_prices(Price(3,50),Price(1,50))
    print(Four_Two)
    Four_Three = add_prices(Price(1,49), Price(1,50))
    print(Four_Three)
    Four_Four = add_prices(Price(1,0), Price(3, 100))
    print(Four_Four)
    # Part 5
    print("Part Five test results")
    top_left = Point(1, 4)
    bottom_right = Point(5, 1)
    rect = Rectangle(top_left, bottom_right)
    Five_One = rectangle_area(rect)
    print(Five_One)
    top_left = Point(-1, 4)
    bottom_right = Point(5, -1)
    rect = Rectangle(top_left, bottom_right)
    Five_Two = rectangle_area(rect)
    print(Five_Two)
    # Part 6
    print("Part Six test results")
    book1 = Book(['Author A', 'Author B'], 'Book 1')
    book2 = Book(['Author A'], 'Book 2')
    book3 = Book(['Author C'], 'Book 3')

    books_list = [book1, book2, book3]

    # Find all books written by 'Author A'
    six_two = books_by_author('Author A', books_list)
    print(six_two)

    book1 = Book(['Author A'], 'Book 1')
    book2 = Book(['Author A'], 'Book 2')
    book3 = Book(['Author B'], 'Book 3')
    book4 = Book(['Author A'], 'Book 4')
    book5 = Book(['Author B'], 'Book 5')
    six_two = books_by_author('Author B', books_list)
    print(six_two)
    # Part 7
    print("Part Seven test results")
    top_left = Point(0, 10)
    bottom_right = Point(10, 0)
    rect = Rectangle(top_left, bottom_right)
    # Compute the bounding circle
    seven_one = circle_bound(rect)
    # Print the resulting bounding circle
    print(seven_one)

    top_left = Point(-2, 4)
    bottom_right = Point(8, -3)
    rect = Rectangle(top_left, bottom_right)
    # Compute the bounding circle
    seven_two = circle_bound(rect)
    # Print the resulting bounding circle
    print(seven_two)
    # Part 8
    print("Part Eight test results")
    employees = [
        Employee("Alice", 3000),
        Employee("Bob", 2500),
        Employee("Charlie", 4000),
        Employee("Dana", 2000)
    ]

    eight_one = below_pay_average(employees)
    print(eight_one)  # Output might be: ['Bob', 'Dana']

    employees = []
    eight_two = below_pay_average(employees)
    print(eight_two)  # Output might be: ['Bob', 'Dana']



if __name__ == '__main__':
    unittest.main()
