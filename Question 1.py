a = 10

a = a + 2

print(a*2)

a = 19

print(a+3)

a = a // 2


import requests

def is_valid_url(url):
    """
    Check if a URL is valid by trying to access it.
    :param url: the URL to check
    :return: True if valid, False otherwise
    """
    try:
        requests.get(url)
        return True
    except:
        return False


print(is_valid_url("https://www.gutenberg.org/cache/epub/43/pg43.txt"))
print(is_valid_url("htp://wrongurl"))



def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

nums = [
    "1414884937242655719669145562427394884141",
    "9847255590886266818998186626880955527489",
    "6800923757255865070000705685527573290086",
    "6892149109325320763773670235239019412986"
]

for n in nums:
    print(n, palindrome(n))




#question 4

numbers = [1, 2, 3]
numbers[1] = 99
print(numbers)

word = "cat"
word[1] = "o"
print(word)

