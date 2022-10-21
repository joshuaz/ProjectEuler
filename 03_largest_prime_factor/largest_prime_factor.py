def largest_prime_factor(number):
    factors = []
    for x in range(1,number+1):
        if number % x == 0:
            factors.append(x)
    
    prime_factors = []
    for y in factors:
        num_of_factors_in_y = []
        for z in range(1,y+1):
            if y % z == 0:
                num_of_factors_in_y.append(z)
                if len(num_of_factors_in_y) == 2:
                    prime_factors.append(z)               
    return(max(prime_factors))