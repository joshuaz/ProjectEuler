sum_of_multiples = 0
for x in range(number):
    if x % 3 == 0 or x % 5 == 0:
        sum_of_multiples += x

print(sum_of_multiples)



def sum_of_multiples(number):
    i = 0
    sum = 0
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            sum +=i
        i += 1
    return(sum)
    
    
print (sum( number for number in range(number) if  (number % 3==0 or number % 5==0) ))
