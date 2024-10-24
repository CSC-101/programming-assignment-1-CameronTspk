from data import *

# Write your functions for each part in the space below.

# Part 1
# Function to count vowels within the word parameter passed into the function
def vowel_count(word: str) -> int:
    vowels = ["a","e","i","o","u"] # includes a string of possible vowels to be counted
    count = 0
    # compares each letter of a word parameter passed in to the possible vowels and adds one to count for each matching vowel
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count


# Part 2
#Comprises a list of all lists of length two
def short_lists(whole_list: list[list[int]])->list[list[int]]:

    shortlist = []
# for every list passed in it will check the length of the list and if its two it will add it to the shortened list
    for sublist in whole_list:
        if len(sublist) == 2:
            shortlist.append(sublist)
    return shortlist

# Part 3
# takes only lists of length two such as the previous but now checks wether the first element of the list is greater than the last and changes their order so that it's in ascending order
def ascending_pairs(unordered: list[list[int]])->list[list[int]]:

    organized_list = []
#Changes order to ascending by checking list length and value of list elements
    for sublist in unordered:
        if len(sublist) == 2 and sublist[0] > sublist[1]:
            x = sublist[0]
            sublist[0] = sublist[1]
            sublist[1] = x
            organized_list.append(sublist)
        else:
            organized_list.append(sublist)
    return organized_list

# Part 4
# adds the values of two prices together by adding dollars and cents and then converting cents over 100 to new dollars
def add_prices(price1: Price, price2: Price) -> Price:
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents
#cents being over 100 converted to a new dollar
    if total_cents > 99:
        total_dollars += (total_cents//100)
        total_cents = total_cents % 100

    return Price(total_dollars, total_cents)
# Part 5
def rectangle_area(rect: Rectangle) -> int:
    # Calculate the width and height of the rectangle
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y

    # Return the area of the rectangle
    return width * height

# Part 6
def books_by_author(author: str, books: list[Book]) -> list[Book]:
    # List to store the books by the specified author
    result = []

    # Loop through the list of books
    for book in books:
        # Check if the author is in the list of authors of the book
        if author in book.authors:
            result.append(book)

    return result

# Part 7
def circle_bound(rectangle: Rectangle) -> Circle:
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    center = Point(center_x, center_y)

    # Calculate the radius (distance from center to one of the corners, e.g., top_left)
    radius = math.sqrt((center_x - rectangle.top_left.x) ** 2 + (center_y - rectangle.top_left.y) ** 2)

    # Return a new Circle object with the calculated center and radius
    return Circle(center, radius)

# Part 8
def below_pay_average(employees: list) -> list[str]:
    if not employees:
        return []

    # Calculate the total pay rate of all employees
    total_pay = sum(employee.pay_rate for employee in employees)
    # Calculate the average pay rate
    average_pay = total_pay / len(employees)

    # Create a list of names of employees whose pay is below the average
    below_average_employees = [employee.name for employee in employees if employee.pay_rate < average_pay]

    return below_average_employees

