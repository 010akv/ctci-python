import argparse

ALLOWED_OPS = ['create','insert','remove']

def parse_my_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--operation',type=str,help='Must be one of - create/insert/remove',default='create')
    parser.add_argument('--elements',nargs='+',help='Elements to add to linked list. Integers, space separated')
    args = parser.parse_args()
    return args()

def validate_args(args):
    if not all(isinstance(e,int) for e in args.elements):
        raise ValueError('Enter a list of space separated ints')
    if not args.operation in ALLOWED_OPS:
        raise ValueError('Enter a valid operaion. Must be one of {}'.format(str(ALLOWED_OPS)))


class Node:
    def __init__(self,this_val=None):
        self.this_val = this_val
        self.next = None
        

class MyLinkedList:
    def __init__(self):
        self.head = Node()

    def insert(self,where='end',pos=None,val=None):
        if where not in ['beg','end','mid']:
            raise ValueError('Invalid insert position. Must be one of beg/end/mid')
        if where == 'end':
            this_node = self.head
            while this_node.next != None:
                this_node = this_node.next 
            this_node.next = Node(val)
        if where == 'beg':
            this_node = Node(val)
            this_node.next = self.head
            self.head = this_node
        if where == 'mid':
            if not pos or not isinstance(pos,int):
                raise ValueError('Enter a valid int pos where to insert the node')
            this_node = self.head
            for i in range(pos):
                if this_node.next == None:
                    raise ValueError('Invalid position. list length is shorter than pos value')
                this_node = this_node.next
            new_node = Node(val)
            new_node.next = this_node.next
            this_node.next = new_node
            
    def remove(self, element=None):
        if not element or not isinstance(element,int): 
            raise ValueError('Enter a valid element to remove')
        
        
        this_node = self.head
        if this_node.this_val == element:
            self.head = self.head.next
        while(this_node.next != None):
            if this_node.next.this_val == element:
                tmp = this_node.next
                this_node.next = this_node.next.next
                del tmp
                return 'Success'
            this_node = this_node.next
        

        raise ValueError('Element to remove not found in list')

                
        
            

def main():
    args = parser.parse_args()
    validate_args(args)
    if args.operation == 'create' and len(args.elements)>0:
        my_ll = MyLinkedList()
        my_ll.head.this_val = args.elements[0]
    elif args.operation == 'insert':
        for i in range(len(args.elements):
            my_ll.insert(args.elements[i])
