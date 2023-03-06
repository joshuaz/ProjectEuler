import itertools

def lexical_permutations(n):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    permutations = list(itertools.permutations(digits))
    separator = ''
    consolidated_permutations = int(separator.join(map(str, permutations[n])))
    return(consolidated_permutations)