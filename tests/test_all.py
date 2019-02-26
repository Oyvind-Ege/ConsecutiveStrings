"""
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
"""

from src.functions import longest_consec

class TestLongestConsec(object):
    def test_no_input(self):
        array = []
        assert longest_consec(array, 2) == ''
    
    def test_no_k(self):
        array = ['does', 'not', 'matter']
        assert longest_consec(array, 0) == ''
    
    def test_k_more_than_n(self):
        array = ['item']
        assert longest_consec(array, 2) == ''
    
    def test_one_consecutive_of_one(self):
        array = ['item']
        assert longest_consec(array, 1) == 'item'

    def test_one_pair(self):
        array = ['first', 'pair']
        assert longest_consec(array, 2) == 'firstpair'
    
    def test_first_two_identical(self):
        array = ['first', 'pair', 'first', 'pair']
        assert longest_consec(array, 2) == 'firstpair'
    
    def test_first_of_two_pairs_correct(self):
        array = ['first', 'pair', '2nd', 'pair']
        assert longest_consec(array, 2) == 'firstpair'
    
    def test_middle_of_two_pairs_correct(self):
        array = ['1st', 'pair', 'second', 'pair']
        assert longest_consec(array, 2) == 'pairsecond'
    
    def test_three_consecutive(self):
        array = ['first', 'second', 'third']
        assert longest_consec(array, 3) == 'firstsecondthird'
    
    def test_first_trio_of_two(self):
        array = ['first', 'second', 'third', '4th']
        assert longest_consec(array, 3) == 'firstsecondthird'
    
    def test_middle_trio_of_six(self):
        array = ['1st', 'second', 'third', 'fourth', '5th']
        assert longest_consec(array, 3) == 'secondthirdfourth'


