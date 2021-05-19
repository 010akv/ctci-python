ITEMS_TO_PUSH = [3,7,5]
class Stack:
    def __init__(self, value):
        self.validate(value)
        print('Init stack with'.format(value))
        self.list = [value]
    
    def validate(self, value):
        if not value:
            raise ValueError('Enter a non-null value to init the stack. You entered - []'.format(value))

    def push(self, value):
        self.validate(value)
        self.list.append(value)

    def pop(self):
        item_to_pop = self.list[len(self.list)-1]
        del self.list[len(self.list)-1]
        return item_to_pop



def main():
    stack = Stack(1)
    for i in range(len(ITEMS_TO_PUSH)):
        print('Pushing {}'.format(ITEMS_TO_PUSH[i]))
        stack.push(ITEMS_TO_PUSH[i])
    for i in range(len(stack.list)):
        print(stack.pop())


if __name__=="__main__":
    main()
        
