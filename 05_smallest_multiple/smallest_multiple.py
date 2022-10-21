import math
def smallest_multiple(num):
    factorial_of_number = math.factorial(num)
    for x in range(1,factorial_of_number):
        list = []
        for y in range(1,num+1):
            if x%y ==0:
                list.append(y)
        if len(list) == num:
            break
    return(x)