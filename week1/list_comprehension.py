def list_comp():
    comprehension = [2**x for x in range(9)]
    # loops through 9 times each time x is a new number (1, 2, 4) and is multiplied by 2 which becomes the new x
    print(comprehension)
#     prints each number that is multiplied up to 9
list_comp()