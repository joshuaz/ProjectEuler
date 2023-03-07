#We can start by writing a function that checks if a number is prime or not:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#Next, we can write a function that calculates the number of consecutive primes that a quadratic expression produces for values of n starting from 0:
def consecutive_primes(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

#Finally, we can write the main function that loops through all possible values of a and b and finds the product of the coefficients that produces the maximum number of consecutive primes:
def quadraticPrimes(n):
    max_primes = 0
    max_product = 0
    for a in range(-n, n):
        for b in range(-n, n):
            num_primes = consecutive_primes(a, b)
            if num_primes > max_primes:
                max_primes = num_primes
                max_product = a * b
    return max_product
