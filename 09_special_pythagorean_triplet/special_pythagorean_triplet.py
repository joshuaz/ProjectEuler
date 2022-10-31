def special_pythagorean_triplet(n):
    p = -1
    for a in range(n//3-1, 2, -1):
        b = n*(n-2*a) // (2*(n-a))
        c = n - a - b
        if a<b and a*a + b*b == c*c: 
            p = a*b*c
            break
    return(p)