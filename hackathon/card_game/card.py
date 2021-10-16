import random
class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''
    
    def __init__(self, laBai1, laBai2, laBai3):
        self._laBai1 = laBai1
        self._laBai2 = laBai2
        self._laBai3 = laBai3

    def __str__(self):
        listValue = [1,2,3,4,5,6,7,8,9]
        self._laBai1 = random.choice(listValue)
        self._laBai2 = random.choice(listValue)
        self._laBai3 = random.choice(listValue)
        
    def __gt__(self, other):
        '''So sánh 2 lá bài'''
