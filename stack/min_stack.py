ELEMENTS_TO_PUSH = [4,3,5,2,1,7,0,9]
class StackWithMin:
    def __init__(self, value):
        self._validate(value)
        self.list = [value]
        self.minval_list = []
        self.minval = value

    def push(self, value):
        self._validate(value)
        self.list.append(value)
        if value < self.minval:
            self.minval_list.append(self.minval)
            self.minval = value

    def _validate(self, value):
        if value==None or not isinstance(value, int):
            raise ValueError('Invalid value. Must be an integer. You entered - {}'.format(value))

    def pop(self):
        pop_idx = len(self.list)-1
        item_to_pop = self.list[pop_idx]
        if item_to_pop == self.minval and len(self.minval_list)!=0:
            self.minval = self.minval_list[len(self.minval_list)-1]
            del self.minval_list[len(self.minval_list)-1]
        del self.list[pop_idx]
        return item_to_pop

    def find_min(self):
        return self.minval
        

def main():
    stackwithmin = StackWithMin(ELEMENTS_TO_PUSH[0])
    for i in range(1, len(ELEMENTS_TO_PUSH)):
        print('Pushing {}'.format(ELEMENTS_TO_PUSH[i]))
        stackwithmin.push(ELEMENTS_TO_PUSH[i])
        print('New min is {}'.format(stackwithmin.find_min()))
    
    for i in range(len(stackwithmin.list)):
        print(stackwithmin.pop())
        print('New min is {}'.format(stackwithmin.find_min()))


if __name__=="__main__":
    main()
