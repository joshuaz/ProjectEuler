import math

def sum_of_divisors(n):
    divisors = set([1])
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return sum(divisors)

def sumOfNonAbundantNumbers(n):
    abundant_numbers = set()
    for i in range(1, n+1):
        if sum_of_divisors(i) > i:
            abundant_numbers.add(i)

    non_abundant_sums = set(range(1, n+1))
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j in non_abundant_sums:
                non_abundant_sums.remove(i+j)

    return(sum(non_abundant_sums))

#Explanation:

# The problem requires us to find the sum of all positive integers that cannot be written as the sum of two abundant numbers. An abundant number is a number whose sum of proper divisors is greater than the number itself.

# To solve this problem, we first define a function sum_of_divisors(n) that returns the sum of all proper divisors of a given number n. We then create a set abundant_numbers containing all abundant numbers between 1 and 28123 (inclusive). We do this by iterating through each number in that range and checking if its sum of divisors is greater than itself. If it is, we add it to the abundant_numbers set.

# Next, we create a set non_abundant_sums containing all integers between 1 and 28123 (inclusive). We then iterate through each pair of abundant numbers and remove their sum from the non_abundant_sums set, since we know that the sum of two abundant numbers is also an abundant number.

# Finally, we print the sum of all remaining numbers in the non_abundant_sums set, which is the answer to the problem.
