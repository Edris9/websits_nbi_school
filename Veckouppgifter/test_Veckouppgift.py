from Veckouppgift5 import *
import unittest

def test_empty_list():
    """
    Test case for empty list scenario.

    Tests the behavior when both expected and actual values are None.

    Returns:
        None

    Asserts:
        Verifies that actual value equals expected value (None == None)
    """
    excepted = None
    actual = None
    assert actual == excepted

def test_number_list():
    """
    Test function for checking sum_list behavior.

    Tests the sum_list function with different test cases:
        - Single element list [5]
        - Multi-element list with varying numbers [1, 2342, 3, 2345]
        - Two element list with identical numbers [2345, 2345]

    Returns:
        None

    Asserts:
        Verifies that all test cases return None
    """
    assert sum_list([5])  is None
    assert sum_list([1, 2342, 3, 2345]) is None
    assert sum_list([2345, 2345]) is None

def test_count_vowels_2_case1():
        """
        Test function for counting vowels in strings.

        Tests the count_vowels function with various test cases:
            - String with vowels ("quit")
            - String without vowels ("Tt")
            - String with numbers ("123 123")
            - Empty string ("")

        Returns:
            None

        Asserts:
            Verifies correct vowel count for each test case
        """
        assert count_vowels("quit") == 2 
        assert count_vowels("Tt") == 0
        assert count_vowels("123 123") == 0
        assert count_vowels("") == 0


def test_count_vowels_2_case3():
    """
    Test function for counting vowels in strings.

    Tests the count_vowels function with:
        - String with all vowels ("AeIoU")
        - String with only Y's ("yYy")

    Returns:
        None

    Asserts:
        Verifies correct vowel count for each test case
    """
    assert count_vowels("AeIoU") == 5
    assert count_vowels("yYy") == 3



def test_subtract():
    """
    Test function for the subtract operation.

    Tests the subtract function by:
        - Subtracting 5 from 10
        - Verifying the result equals 5

    Returns:
        None

    Asserts:
        Verifies that actual result matches expected value (10 - 5 = 5)
    """
    x = 10
    y = 5
    excepted = 5
    actual = subtract(10, 5)
    assert actual == excepted



def test_largest_digit():
    """Test function for finding the largest digit in a list.

    Tests the larg_digit function with various test cases:
        - Regular sequence of increasing numbers [1,2,3,4,5]
        - List of multiples of 10 [10,20,30]
        - List with negative numbers [0,-1,-5]
        - List with a large number [1000,1,2]
        - List with identical numbers [5,5,5]

    Returns:
        None

    Raises:
        AssertionError: If any test case fails
    """
    assert larg_digit([1,2,3,4,5]) == 5
    assert larg_digit([10,20,30]) == 30 
    assert larg_digit([0,-1,-5]) == 0
    assert larg_digit([1000,1,2]) == 1000
    assert larg_digit([5,5,5]) == 5


def test_find_2nd_larg_digit():
        """
        Test function for finding the second largest digit in a list.

        Tests the find_2nd_large function with:
            - List of integers [32,554,34,65,87,45,50]
            - Verifies that 87 is the second largest value

        Returns:
            None

        Asserts:
            Verifies that the second largest value is 87
        """
        assert find_2nd_large([32,554,34,65,87,45,50]) == 87


def test_c_to_f():
    """
    Test function for c_to_f conversion.

    Tests the c_to_f function with various test cases:
        - Valid temperature (10°C)
        - Temperature below absolute zero (-300°C)
        - Freezing point of water (0°C)
        - Boiling point of water (100°C)
        - Negative temperature (-40°C)

    Returns:
        None

    Asserts:
        Verifies correct Fahrenheit conversion for each test case
    """
    # Valid temperature
    degree = 10
    expected = 50
    actual = c_to_f(degree)
    assert actual == expected

    # Temperature below absolute zero
    degree = -300
    expected = None
    actual = c_to_f(degree)
    assert actual == expected

    # Freezing point of water
    degree = 0
    expected = 32
    actual = c_to_f(degree)
    assert actual == expected

    # Boiling point of water
    degree = 100
    expected = 212
    actual = c_to_f(degree)
    assert actual == expected

    # Negative temperature
    degree = -40
    expected = -40
    actual = c_to_f(degree)
    assert actual == expected



def test_count_words():
    # AK1: Enkla meningar
    assert count_words("Hej på dig") == 3

    # AK2: Flera mellanslag
    assert count_words("Hej   på   dig") == 3

    # AK3: Tom sträng
    assert count_words("") == 0

    # AK4: Mellanslag i början/slut
    assert count_words(" Hej på dig ") == 3

    # AK5: Inga mellanslag
    assert count_words("Hej") == 1

    print("Alla testfall godkända!")

