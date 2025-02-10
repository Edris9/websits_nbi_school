# Returnerar summan av alla tal i listan
def sum_list(list):
    return None



def count_vowels(word):
    return None



def count_vowels(word):
    return sum(1 for char in word.lower() if char in "aeiouy")



def subtract(x,y):
    return x - y 


def larg_digit(list_digit=None):
    if list_digit is None:
        list_digit = [1, 2, 3, 4, 5] 
    largest = max(list_digit)
    return largest





def find_2nd_large(numbers=None):
    numbers = [32,554,34,65,87,45,50]
    for i in numbers:
        if i == sorted(numbers)[-2]:
            return i
