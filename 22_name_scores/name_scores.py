import urllib
from urllib.request import urlopen
import string
def nameScores(arr):
    alphabet = string.ascii_uppercase
    data = urlopen('https://projecteuler.net/project/resources/p022_names.txt')
    txt = data.read()
    lines = str(txt).split(",")  # Opening the file and assigning the string to "lines"
    lines = sorted(lines)
    lines
    total_score = 0
    for index, line in enumerate(lines, start=1):
        total_score += index * sum(alphabet.find(c)+1 for c in line)
    
    return(total_score)


#from string import ascii_uppercase as upper
#total_score = 0
#data = urlopen('https://projecteuler.net/project/resources/p022_names.txt')
#txt = data.read()
#lines = str(txt).split(",")  # Opening the file and assigning the string to "lines"
#L1 = sorted([_.strip('"') for _ in lines]) # Removes the individual quotes and sorts the list as well
#for i in L1:
#    letter_score = sum([upper.find(j)+1 for j in i]) # Sums up the index of individual letters in the words so as to get letter score
#    total_score += letter_score*(L1.index(i)+1)
#print(total_score)
