def isPalindrome(s):
    return s == s[::-1]

def largest_palindrome_product(num):
    top_num = 10**num
    bottom_num = 10**(num - 1)

    num_1 = range(bottom_num,top_num)
    num_2 = range(bottom_num,top_num)
    list_of_palindromes = []         
    for x in num_1:
        for y in num_2:
            is_this_number_a_palindrome_string = str(x * y)
            is_this_number_a_palindrome_number = x*y
            ans = isPalindrome(is_this_number_a_palindrome_string)
            if ans:
                list_of_palindromes.append(is_this_number_a_palindrome_number)

    return(max(list_of_palindromes))