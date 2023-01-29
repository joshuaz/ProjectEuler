def sumAmicableNum(x):
    # Use set instead
    amicable_numbers = set()

    # No point assigning the range to a variable
    for num in range(1, x):
        x_val = 0
        y_val = 0

        # No point assigning the range to a variable
        for val in range(1, num):
            if (num % val) == 0:
                x_val += val

        for val in range(1, x_val):
            if (x_val % val) == 0:
                y_val += val

        # Also check if x_val NOT equal to y_val
        if y_val == num and x_val != y_val:
            amicable_numbers.add(y_val)

    return sum(amicable_numbers)