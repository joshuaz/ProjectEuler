def powerDigitSum(exponent):
    value_to_break_into_smaller_digits = 2**exponent
    list_of_digits = [int(i) for i in str(value_to_break_into_smaller_digits)]
    sum_of_digits = sum(list_of_digits)
    return(sum_of_digits)