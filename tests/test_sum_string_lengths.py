from src.functions import sum_string_lengths

class TestSumStringLengths(object):
    def test_one(self):
        array = ['onestring']
        assert sum_string_lengths(array) == [9]
    
    def test_two(self):
        array = ['one', 'two', 'eighteen']
        assert sum_string_lengths(array) == [3, 3, 8]
 