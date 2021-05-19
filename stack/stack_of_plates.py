MAX_STACK_SIZE = 3
ELEMENTS_TO_PUSH = [1,3,4,5,0,9,8]

class SetOfStacks:
    def __init__(self, value):
        self._validate(value)
        self.lists = [[value]]
        self.curr_substack_idx = 0
    
    def _validate(self, value):
        if value==None or not isinstance(value, int):
            raise ValueError('Value must be a valid integer, but you entered - {}'.format(value))
        
    def push(self,value):
        self._validate(value)
        if len(self.lists[self.curr_substack_idx]) < MAX_STACK_SIZE:
            self.lists[self.curr_substack_idx].append(value)
        else:
            new_list = [value]
            self.lists.append(new_list)
            self.curr_substack_idx += 1
            
    def pop(self):
        pop_idx = len(self.lists[self.curr_substack_idx])-1
        item_to_pop = self.lists[self.curr_substack_idx][pop_idx]
        del self.lists[self.curr_substack_idx][pop_idx]
        if len(self.lists[self.curr_substack_idx])==0:
            self.curr_substack_idx -= 1


    def popAt(self, index):
        pop_idx = len(self.lists[index])-1
        if pop_idx <0:
            raise ValueError('This sub stack is empty. Try a different index')
        item_to_pop = self.lists[index][pop_idx]
        del self.lists[index][pop_idx]
        return item_to_pop 
