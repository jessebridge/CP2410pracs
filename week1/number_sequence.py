from collections import Counter


def number_sequence():
    numbers_list = [1, 5, 6, 3, 2, 1, 5, 6, 7]
    # list of numbers
    counter = Counter(numbers_list)
    # Uses an in built module to count through each item in the list and see if they are the same
    print(counter)
    # prints the list of each number and how many times it has been used
    result = [i for i, j in counter.items() if j > 1]
    # List comprehension, loops through the list and finds if the 2nd attribute of the list is more than 1
    # Meaning there is more than 1 of that number
    print(result)
#     prints the numbers that have more than 1 occurrence
number_sequence()
