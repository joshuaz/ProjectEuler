import math
def sum_square_difference(num):
    sum_of_squares = 0
    for x in range(1,num+1):
        sum_of_squares += x**2
    square_of_sums = 0
    for y in range(1,num+1):
        square_of_sums += y
    
    return((square_of_sums**2) - sum_of_squares)