import math
def sumFactorialDigits(n):
    value_to_break_into_smaller_digits = math.factorial(n)
    list_of_digits = [int(i) for i in str(value_to_break_into_smaller_digits)]
    sum_of_digits = sum(list_of_digits)
    return(sum_of_digits)