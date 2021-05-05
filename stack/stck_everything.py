STACK_SIZE_THRESHOLD = 2
class Stack:
    def __init__(self, value):
        self.validate(value)
        self.list = [value]
   
    def validate(self, value): 
        print('validating...',value)
        if not value or not isinstance(value,int):
            raise ValueError('Enter a valid int to init the stack')
    
    def push(self, value):
        self.validate(value)
        self.list.append(value)
    
    def pop(self):
        top_idx = len(self.list) - 1
        top_tmp = self.list[top_idx]
        del self.list[top_idx]
        return top_tmp        

    def display(self):
        print('Wanna take a look at the Stack?')
        for stack_elem in reversed(self.list):
            print(stack_elem)



class SetOfStacks():
    def __init__(self, value):
        self.stacks = []
        self.curr_stack = Stack(value)
        self.stacks.append(self.curr_stack)
        self.curr_size = 1
        self.curr_stack_idx = 0
    
    def validate(self, value): 
        print('validating...',value)
        if not value or not isinstance(value,int):
            raise ValueError('Enter a valid int to init the stack')
    
    def push(self, value):
        self.validate(value)
        if len(self.curr_stack.list) >= STACK_SIZE_THRESHOLD:
            print('Creating a new stack for ', value)
            self.curr_stack = Stack(value)
            self.curr_stack_idx += 1
            self.stacks.append(self.curr_stack)
        self.curr_stack.push(value)
    
    def pop(self):
        print('Num stakcs we got - ',len(self.stacks))
        this_elem = self.stacks[self.curr_stack_idx].pop()
                        
        print('Curr stacj len',len(self.stacks[self.curr_stack_idx].list))
        return this_elem
            
            
    
def main():
    new_stack = Stack(1)
    new_stack.push(3)
    new_stack.push(5)
    new_stack.display()
    print('Popping top 2 elements')
    print(new_stack.pop())
    print(new_stack.pop())
    print('Stack after popping')
    new_stack.display()
    print('Creating a set of stacks')
    set_of_stacks = SetOfStacks(1)
    for i in range(2,6):
        set_of_stacks.push(i)
    for i in range(5):
        print('I popped',set_of_stacks.pop())

if __name__ == "__main__":
    main()
