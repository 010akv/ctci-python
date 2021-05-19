STACK_LIST = list()
STACK_SIZES = []
STACK_1_ITEMS = [4,5,6]
STACK_2_ITEMS = [9,0]
STACK_3_ITEMS = [7,8,9]



class StackUsingSingleArray:
    def __init__(self, value, size):
        self.validate(value)
        self.idx = len(STACK_SIZES)
        STACK_SIZES.append(size)
        this_start_idx = 0
        for i in range(self.idx):
            this_start_idx += STACK_SIZES[i]
        STACK_LIST.insert(this_start_idx,value)
        self.top_idx = this_start_idx

    def validate(self, value):
        if not value:
            raise ValueError('Enter a valid value to push to  the stack. you entered - {}'.format(value))    

    def push(self, value):
        self.validate(value)
        self.top_idx += 1
        STACK_LIST.insert(self.top_idx, value)

    def pop(self):
        item_to_pop = STACK_LIST[self.top_idx]
        del STACK_LIST[self.top_idx]
        self.top_idx -= 1
        return item_to_pop

def main():
    stack_one = StackUsingSingleArray(1, 3)
    for i in range(len(STACK_1_ITEMS)):
        print('Pushing to stack 1 - {}'.format(STACK_1_ITEMS[i]))
        stack_one.push(STACK_1_ITEMS[i])
    for i in range(STACK_SIZES[0]):
        print(stack_one.pop())

if __name__=="__main__":
    main()
           
