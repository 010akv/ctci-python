import argparse


SUPPORTED_OPERATIONS = [None,'insert','delete','display']

class GetInputs:
    
    def __init__(self):
        pass

    def parse_my_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--hash_table_size',help='Size of the hash table (num lists)', type=int)
        parser.add_argument('--operation',help='insert/delete/display',type=str)
        parser.add_argument('--key',help='Key to insert/delete',type=int)
        parser.add_argument('--value',help='Value to insert/delete',type=int)
        self.args = parser.parse_args()
        self._validate_my_args()
        return self.args    
    
    def _validate_my_args(self):
        if self.args.operation not in SUPPORTED_OPERATIONS:
            raise ValueError('operation must be one of {}'.format(SUPPORTED_OPERATIONS))
        if self.args.operation in ['insert','delete']:
            if not isinstance(self.args.key,int):
                raise ValueError('Key must be a valid int. You entered {}'.format(key))
        

class MyNestedListHashTable:
    def __init__(self, size):
        if not isinstance(size,int):
            raise ValueError('Size must be a valid integer. You entered {}'.format(size))
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
    
    def hash_the_key(self, key):
        if not isinstance(key,int):
            raise ValueError('key must be a valid integer. You entered {} which is invalid'.format(key))
        index = key % self.size
        return index
    
    def insert(self, key, value, display = False):
        index = self.hash_the_key(key)
        if value is None or value == '':
            raise ValueError('Value to insert cannot be empty. You entered {}'.format(value))
        self.hash_table[index].append(value)
        print('{} inserted at index {}'.format(value, index))
        if display:
            self.display()        

    def delete(self, key):
        index = self.hash_the_key(key)
        self.hash_table[index] = []

    def display(self,format_it_nicely=False):
        if format_it_nicely:
            for i in range(len(self.hash_table)): 
                print(i, end = " ") 
                  
                for j in self.hash_table[i]: 
                    print("-->", end = " ") 
                    print(j, end = " ") 
                print()
        else:
            print(self.hash_table)
       


def main():
    get_inputs = GetInputs()
    args = get_inputs.parse_my_args()

    hash_table = MyNestedListHashTable(args.hash_table_size)
    hash_table.display()

    if args.operation == 'insert':
        hash_table.insert(args.key,args.value, display=True)

if __name__=="__main__":
    main()
