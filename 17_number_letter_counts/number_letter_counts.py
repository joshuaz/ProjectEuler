import inflect

p = inflect.engine()

def numberLetterCounts(limit):

    total_length_of_all_words = 0

    for i in range(1, limit+1):

        word = p.number_to_words(i)

        word = word.replace(" ", "")

        word = word.replace("-", "")

        length_of_word = len(word)

        total_length_of_all_words = total_length_of_all_words + length_of_word

    return(total_length_of_all_words)