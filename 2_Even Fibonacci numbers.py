def fib(number):
    x, y = 0, 1
    sum_even_numbers = 0
    while x+y < number:
        x, y = y, x+y
        if y % 2 ==0:
            sum_even_numbers += y
    return(sum_even_numbers)
