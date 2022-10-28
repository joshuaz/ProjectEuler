def what_is_the_10001st_prime(number):
    i = 1
    list_of_primes = []
    while len(list_of_primes) <= number: 
        for x in range(2, int(i/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (i % x) == 0:
                break
        else:
            list_of_primes.append(i)
        i +=1
    return(max(list_of_primes))