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


#The script uses three functions:
#sum_of_divisors(n): This function calculates the sum of proper divisors of a given number n.
#find_abundant_numbers(limit): This function finds all abundant numbers up to a given limit. An abundant number is a number whose sum of proper divisors is greater than the number itself.
#is_sum_of_abundant_numbers(n, abundant_numbers): This function checks if a given number n can be written as the sum of two abundant numbers from a given list of abundant numbers.
#The main part of the script first finds all abundant numbers up to 28123 using the find_abundant_numbers() function. It then uses the is_sum_of_abundant_numbers() function to find all numbers that cannot be written as the sum of two abundant numbers. Finally, it calculates the sum of all such numbers using the sum() function and prints the result.
