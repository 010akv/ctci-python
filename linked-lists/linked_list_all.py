class Node:
    def __init__(self, value):
        if not value:
            raise ValueError('Need at least one value to init a Node')
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        if not value or not isinstance(value,int):
            raise ValueError('Need at least one valid int to init the linked list')
        self.head = Node(value)
        self.curr = self.head

    def insert(self, value):
        if not value or not isinstance(value,int):
            raise ValueError('Value to insert is empty/not an int')
        
        new_node = Node(value)
        self.curr.next = new_node
        self.curr = new_node 
    
    def display(self):
        this = self.head
        while this:
            print(this.value)
#            print('\n|\nV\n')
            this = this.next
                    

    def remove_first_occurence(self, value):
        if not value or not isinstance(value,int):
            raise ValueError('Value to insert is empty/not an int')

        if self.head.value == value:
            self.head = self.head.next
            return "removed {}".format(value)
        this = self.head
        print(this.value)
        while this.next:
            if this.next.value == value:
                this.next = this.next.next
                return "removed {}".format(value)
            this = this.next
        return 'Value {} not in list, cannot be removed!'.format(value)

    def remove_dups(self):
        ll_values = []
        this = self.head
        ll_values.append(head.value)
        while this.next:
            if this.next.value in ll_values:
                this.next = this.next.next
            else:
                ll_values.append(this.next.value)
    
    def remove_dups_no_buffer(self):
        this = self.head
        checker = self.head
        while this:
            while checker.next:
                if checker.next.value == this.value:
                    checker.next = checker.next.next
                checker = checker.next
            this = this.next

    def remove_node(self, node):
        if not node:
            raise ValueError('Node to remove is empty')
        node.value = node.next.value
        node.next = node.next.next


    def return_k_to_last(self, k):
        this = self.head
        ret_values = []
        counter = 0
        while this:
            this = this.next
            counter += 1
            if counter > k:
                ret_values.append(this.value)
        return ret_values

    def del_mid_node(self):
        ll_len = 0
        this = self.head
        while this:
            ll_len += 1
            this = this.next
        mid_id = ll_len // 2
        counter = 0
        this = self.head
        while this:
            if counter == mid_id-1:
                this.next = this.next.next
                return 0
            this = this.next
            counter += 1
    
    def part_around_x(self, x):
        this = self.head
        while this.next:
            print('Now at',this.value, this.next.value)
            if this.next.value < x:
                tmp = this.next
                this.next = this.next.next
                tmp.next = self.head
                self.head = tmp     
            else:
                this = this.next
        
    def check_palindrome(self):
        this = self.head
        ll_values = []
        while this:
            ll_values.append(this.value)
            this = this.next    
        
        ll_len = len(ll_values)
        half_idx = ll_len // 2        

        for i in range(half_idx):
            if ll_values[i] != ll_values[ll_len-i]:
                return False
        
        return True
            
    
    def find_loop(self):
        this = self.head
        visited_nodes = []
        while this:
            if this in visited_nodes:
                return this
            visited_nodes.append(this)   
            this = this.next

    def find_loop_efficient(self):
        fast_runner = slow_runner = self.head
        while fast_runner and fast_runner.next:
            if slow_runner == fast_runner:
                break
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
        
        
        
def find_num_from_ll(ll, order='rev'):
    this = ll.head
    idx = 0
    num = 0
    ll_len = 0
    if order == 'forw':
        while this:
            ll_len += 1
            this = this.next
        this = ll.head
        print('len ll=',ll_len)
    while this:
        if order == 'rev':
            num += this.value * (10 ** idx)
        else:
            num += this.value * (10 ** (ll_len-1-idx))
        idx += 1
        this = this.next
    return num

def sum_nums_as_ll(ll1, ll2, order='rev'):
    num1 = find_num_from_ll(ll1, order=order)
    num2 = find_num_from_ll(ll2, order=order)
    return num1 + num2 
            


def check_intersect(ll1, ll2):
    ptr1 = ll1.head 
    ptr2 = ll2.head
    while ptr1:
        while ptr2:
            if ptr1 == ptr2:
                return True
            ptr2 = ptr2.next
        ptr1 = ptr1.next    


def main():
    ll = LinkedList(1)
    ll.insert(5)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(1)
    ll.insert(4)
    ll.display() 
    print('Trying to remove 4')
    ll.remove_first_occurence(4)
    ll.display()
    print('Part around {}'.format(3))
    ll.part_around_x(5)
    ll.display()
    print('Summing')
    ll1 = LinkedList(7)
    ll1.insert(1)
    ll1.insert(6)
    print('LL1:')
    ll1.display()
    ll2 = LinkedList(5)
    ll2.insert(9)
    ll2.insert(2)
    print('LL2')
    ll2.display()
    sum_lls = sum_nums_as_ll(ll1, ll2)
    print('Summing forward')
    sum_lls = sum_nums_as_ll(ll1, ll2, order='forw')
    print('Sum:',sum_lls)

if __name__=="__main__":
    main()
     
