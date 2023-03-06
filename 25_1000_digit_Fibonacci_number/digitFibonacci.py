def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def digitFibonacci(digits):
    f = fibonacci()
    for index, fibonacci_number in enumerate(f):
        if len(str(fibonacci_number)) == digits:
            #print("The index of the first term in the Fibonacci sequence to contain", digits, "digits is:", index+1)
            break
    return(index)

#In this script, we define a generator function fibonacci that yields the Fibonacci sequence indefinitely. We then create a generator object f using the fibonacci function.

#We then loop through the f generator using the enumerate function to keep track of the index of each Fibonacci number. When we find a Fibonacci number with digits number of digits, we print the index and break out of the loop.

#Note that we add 1 to the index before printing it, as the problem statement asks for the index starting from 1 rather than 0.