def longestCollatzSequence(limit):
    highest_count_thus_far = 1
    for x in range(1, limit + 1):
        count = 1
        collatz_number = x
        while collatz_number != 1:
            if collatz_number % 2 == 0:
                collatz_number = collatz_number/2
            else:
                collatz_number = (3 * collatz_number) + 1
            count += 1
        if count > highest_count_thus_far:
            highest_count_thus_far = count
            current_highest_collatz_number = x
    return(current_highest_collatz_number)