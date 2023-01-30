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