INPUT_LIST = [-5, 6, 8, 9, 3, 4, 5, 7]


class Node:
    def __init__(self,val=None,left=None,right=None):
        self.validate(val)

    def validate(self, val):
        if val==None or not isinstance(val,int):
            raise ValueError('Enter a valid integer. You entered {} - invalid'.format(val))
