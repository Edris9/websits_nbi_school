# This function calculates and returns the sum of all numbers in the given list
def sum_list(list):
    return None



def count_vowels(word):
    # Takes a word as input and returns the number of vowels in the word
    return None



# Takes a word as input and returns the number of vowels in the word
def count_vowels(word):
    return sum(1 for char in word.lower() if char in "aeiouy")



# This function subtracts two numbers and returns the difference
def subtract(x,y):
    return x - y 


def larg_digit(list_digit=None):
    # If no list is provided, use default list [1, 2, 3, 4, 5]
    if list_digit is None:
        list_digit = [1, 2, 3, 4, 5] 
    # Find and return the largest number in the list using max() function
    largest = max(list_digit)
    return largest





def find_2nd_large(numbers=None):
    """
    Find the second largest number in a list of integers.

    The function takes an optional parameter 'numbers' but uses a hardcoded list [32,554,34,65,87,45,50].
    Returns the second largest number in the list by comparing each number with the second-to-last element
    of the sorted list.

    Parameters:
        numbers (list, optional): List of integers (not used due to hardcoded list)

    Returns:
        int: The second largest number in the hardcoded list

    Example:
        >>> find_2nd_large()
        87  # Since 554 is largest, 87 is second largest in [32,554,34,65,87,45,50]
    """
    numbers = [32,554,34,65,87,45,50]
    for i in numbers:
        if i == sorted(numbers)[-2]:
            return i


def c_to_f(degree):
    """ 
    ekvivalensklasser 

    Invalid Input:

    Values less than -273.15°C (absolute zero).

    Examples: -300, -1000.

    Behavior: The function returns None.

    Valid Input:

    Values greater than or equal to -273.15°C.

    Examples: 0, 100, -273.15, 25.5.

    Behavior: The function returns the corresponding temperature in Fahrenheit.
        
    """
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32


def count_words(words):
    # Strip whitespace from start/end and split on any number of spaces
    if not words.strip():
        return 0
    return len(words.strip().split())
