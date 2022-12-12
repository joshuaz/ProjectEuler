def divisibleTriangleNumber(n):
    counter = 1
    triangle_number = 1
    divisors = []
    num_divisors = 0
    while num_divisors <= n:
        counter += 1
        triangle_number = triangle_number + counter
        for x in range(1, triangle_number+1):
            if triangle_number % x == 0:
                divisors.append(x)  
        num_divisors = len(divisors)
        divisors = []
    return(triangle_number)
    