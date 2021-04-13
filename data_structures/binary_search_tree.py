

INPUT_LIST = [9,0,8,7,5,6,1,3,2]

class Node:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self, headval=None):
        print(headval, type(headval))
        self.validate(headval)
        self.head = Node(headval)
        self.depth = 1
    
    def validate(self,val):
        if val==None or not isinstance(val, int):
            raise ValueError('Invalid value to insert. Enter a valid integer')
   
    def insert(self, val=None):
        print('trying to insert {}'.format(val),type(val))
        self.validate(val)    
        this_node = self.head
        while 1:
            if val > this_node.val:
                if this_node.right == None:
                    this_node.right = Node(val)
                    if this_node.left == None:
                        self.depth += 1
                    return 'Success'
                else:
                    this_node = this_node.right
            elif val < this_node.val:
                if this_node.left == None:
                    this_node.left = Node(val)
                    if this_node.right == None:
                        self.depth += 1
                    return 'Success'
                else:
                    this_node = this_node.left  
            else:
                raise ValueError('{} already exists in the tree. Cannot insert duplicate node'.format(val))


    def find(self, val=None):
        self.validate(val)
        
        this_node = self.head
        
        while this_node.val != val:
            if val > this_node.val:
                if this_node.right == None:
                    result_str =  'Could not find {} in tree'.format(val)
                    print(result_str)
                    return result_str
                this_node = this_node.right
            else:
                if this_node.left == None:
                    result_str =  'Could not find {} in tree'.format(val)
                    print(result_str)
                    return result_str
                this_node = this_node.left
        
        result_str =  'Found {}'.format(val)
        print(result_str)
        return result_str
    """
    left = 2 
    left.left = 0
    left.right = 3
    root = 5
    right = 7
    right.left = 6 


    this = 5
    res + inorder(2)
    res + inorder(0)  = [] + 
    """
    def inorder(self,this=None):
        res = []
        if this:
            res = inorder(this.left)
            res.append(this.val)
            res = res + inorder(this.right)
        return res
    
    def preorder(self, this=None):
        res = []
        if this:
            res.append(this.val)
            res = res + preorder(this.left)
            res = res + preorder(this.right)
        retuirn res

    def postorder(self, this=None):
        res = []
        if this:
            res = postorder(this.lefT)
            res = res + postorder(this.right)
            res.append(this.val)
        return val

       
 
    def traverse(self,order = 'inorder'):
        if order not in ['inorder','preorder','postorder']:
            raise ValueError('Traversal order should be one of inorder/preorder/postorder. You entered {} - invalid'.format(order))
        this = self.head
        if order == 'inorder':
            res = self.inorder()
        elif order == 'preorder':
            res = self.preorder()
        else:
            res = self.postorder()    
            

def main():
    bst = BinarySearchTree(12)
    for i in INPUT_LIST:
        bst.insert(i)
    bst.find(INPUT_LIST[5])
    bst.find(-8)
    bst = BinarySearchTree('a')


if __name__=="__main__":
    main()
