def find_longest_c_word(filename):
    """
    Find the longest word that starts with 'c' in a text file
    :param filename: the name of the file to search
    :return: the longest word starting with 'c'
    """
    longest_word = ""
    special_characters = ",.?!"

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower()


            for c in special_characters:
                line = line.replace(c, "")

            words = line.split()

            for word in words:
                # check if word starts with 'c'
                if word.startswith("c"):
                    # check if it is longer than current longest
                    if len(word) > len(longest_word):
                        longest_word = word

    return longest_word


print(find_longest_c_word("book.txt"))

#first I start by defining my function. Then I open the file and sort the data in a way that I take the lower case so that the function isn't confused with C anc c.
#then I remove any special characters in the text and punctuation that distorts length.
#lastly, I check for words that start with c and if it is longer than the previous ones found.
