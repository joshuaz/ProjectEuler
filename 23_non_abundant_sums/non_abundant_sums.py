import math

# Function to calculate the sum of proper divisors of a number
def sum_of_divisors(n):
    s = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
    return s

# Function to find abundant numbers up to a given limit
def find_abundant_numbers(limit):
    abundant_numbers = []
    for n in range(12, limit):
        if sum_of_divisors(n) > n:
            abundant_numbers.append(n)
    return abundant_numbers

# Function to check if a number can be written as the sum of two abundant numbers
def is_sum_of_abundant_numbers(n, abundant_numbers):
    for i in range(len(abundant_numbers)):
        if abundant_numbers[i] > n/2:
            return False
        if n - abundant_numbers[i] in abundant_numbers:
            return True
    return False

# Find all abundant numbers up to 28123
abundant_numbers = find_abundant_numbers(28123)

# Find all numbers that cannot be written as the sum of two abundant numbers
not_sum_of_abundant_numbers = []
for n in range(1, 28124):
    if not is_sum_of_abundant_numbers(n, abundant_numbers):
        not_sum_of_abundant_numbers.append(n)

# Calculate the sum of all numbers that cannot be written as the sum of two abundant numbers
print(sum(not_sum_of_abundant_numbers))

def sumOfNonAbundantNumbers(i):
    not_sum_of_abundant_numbers = []
    abundant_numbers = find_abundant_numbers(i)
    for n in range(1, i+1):
        if not is_sum_of_abundant_numbers(n, abundant_numbers):
            not_sum_of_abundant_numbers.append(n)

    return(sum(not_sum_of_abundant_numbers))