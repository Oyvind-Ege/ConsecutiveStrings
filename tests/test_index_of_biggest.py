from src.functions import index_of_biggest

class TestIndexofBiggest(object):

    def test_single_item(self):
        array = [1]
        assert index_of_biggest(array) == 0
    
    def test_multiple(self):
        array = [14,17,14,12]
        assert index_of_biggest(array) == 1
    
    def test_three(self):
        array = [20,20,17]
        assert index_of_biggest(array) == 0
