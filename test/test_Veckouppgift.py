from Veckouppgift5 import *
import unittest

def test_empty_list():
    excepted = None
    actual = None
    assert actual == excepted

def test_number_list():
    assert sum_list([5])  is None
    assert sum_list([1, 2342, 3, 2345]) is None
    assert sum_list([2345, 2345]) is None


def test_count_vowels_2_case1():
    assert count_vowels("quit") == 2 
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0


def test_count_vowels_2_case3():
    assert count_vowels("AeIoU") == 5
    assert count_vowels("yYy") == 3



def test_subtract():
    x = 10
    y = 5
    excepted = 5
    actual = subtract(10, 5)
    assert actual == excepted



def test_largest_digit():
    assert larg_digit([1,2,3,4,5]) == 5
    assert larg_digit([10,20,30]) == 30 
    assert larg_digit([0,-1,-5]) == 0
    assert larg_digit([1000,1,2]) == 1000
    assert larg_digit([5,5,5]) == 5




def test_find_2nd_larg_digit():
    assert find_2nd_large([32,554,34,65,87,45,50]) == 87
