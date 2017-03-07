def is_multiple(n,m):
    if n % m == 0:
        # if n modulo m = 0 then n is a multiple of m
        print("true")
        return True
    # if n is a multiple of m then returns true
    else:
        print("false")
        return False
#     if n is not a multiple of m then returns false
is_multiple(10,3)