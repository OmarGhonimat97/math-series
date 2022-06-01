

def fibonnaci(n):
    if n==0:
        return 0
    elif n < 0:
        return n
    elif n==1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
"""
Return the fibonnaci number of the nth order.
Inputs an integar (n)
calculates the fibonnaci number of the nth order and returns the fibonnaci number
"""

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n < 0:
        return n
    else:
        return lucas(n - 1) + lucas(n - 2)
"""
Return the lucas number of the nth order.
Inputs an integar (n)
calculates the lucas number of the nth order and returns the lucas number
"""

def sum_series(n, first=0, second=1):

    if n==0:
        return first
    elif n==1:
        return second
    elif n < 0:
        return n
    else:
        return sum_series(n-1, first=first, second=second) + sum_series(n-2, first=first, second=second)
"""
Return the sum_series number of the nth order.
Inputs an integar (n) and two optional arguments called first and second, these are the first two numbers
of our series
calculates the sum_series number of the nth order depending on the first and second number of the series
and return the sum_series number 
"""