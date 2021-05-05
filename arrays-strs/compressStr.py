"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
"""

import argparse


def parse_my_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inp_str',help='Input string, only a-z/A-Z')
    args = parser.parse_args()
    return args


class Queue:
    def __init__(self):
        self.first_id = 0
        self.current_id = 0    
        self.list = []

    def insert(self, element):
        self.list[self,current_id] = element
        self.current_id += 1
        return 0
    
    def remove(self, element, rem_id):
        if (not element and not rem_id):
            raise ValueError('Element or rem_id should be valid')
        if element in self.list:
            self.list.remove(element)
        


     

def compress(inp_str):
    if not inp_str:
        return None
    sorted_inp_str = sorted(inp_str)
    queue = Queue()
    char_cnt = 0
    for char in sorted_inp_str:
        if char not in queue.list:
            if queue.list:
                queue.list.append(char_cnt)
            queue.list.append(char)
            char_cnt = 1
        else:
            char_cnt += 1
    queue.list.append(char_cnt)
    if len(queue.list) < len(sorted_inp_str):
        return ''.join([str(char) for char in queue.list])
    else:
        return inp_str
                
    

def main():
    args = parse_my_args()
    compressed = compress(args.inp_str)
    print(compressed)


if __name__=="__main__":
    main()
