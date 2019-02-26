from src.functions import sum_sequence

class TestSumSequenceFunc(object):
    
    def test_simple_pair(self):
        array = [4,7]
        assert sum_sequence(array, 2) == [11]
    
    def test_pairs(self):
        array = [4,7,5,4,4,3,5,7]
        assert sum_sequence(array, 2) == [11, 12, 9, 8, 7, 8, 12]
    
    def test_simple_trio(self):
        array = [5,6,5]
        assert sum_sequence(array, 3) == [16]
    
    def test_long_trio(self):
        array = [3,6,5,6,3]
        assert sum_sequence(array, 3) == [14,17,14]