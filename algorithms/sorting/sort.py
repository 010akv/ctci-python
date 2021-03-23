from random import randint
import time
import argparse


MAX_INP_ARRAY_LEN = 1000


def parse_my_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inp_array_len',type=int,help='Enter an integer - size of array to be sorted, max = {}'.format(MAX_INP_ARRAY_LEN))
    args = parser.parse_args()
    return args

def swap_arith(a,b,op='ad_sub'):
    if op=='ad_sub':
        a = a+b
        b = a-b
        a = a-b
        return a,b
    if op=='mul_div':
        a = a*b
        b = a/b
        a = a/b
        return a,b

"""
Bubble Sort
5, 2, 4, 1, 6

i=0
2, 5, 4, 1, 6
2, 4, 5, 1, 6
2, 4, 1, 5, 6
2, 4, 1, 5, 6

i=1
2, 4, 1, 5, 6
2, 1, 4, 5, 6
2, 1, 4, 5, 6

i=2
1, 2, 4, 5, 6
1, 2, 4, 5, 6

i=3
1, 2, 4, 5, 6

n=4

outer loop: i:
- iterate n times
- take care of one element (the largest in the array)'s position each time
    - eg. i=0, put element at i=0 in its final position (left of i should be < and right should be >)

inner loop: i:
- only go up to n-i-1 
- keep moving the element orig at i until it reaches its final position

i=0,j=0->3
compare j,j+1
compare j+1.j+2
compare j+2,j+3

i=1,j=0->2
compare j,j+1
compare j+1,j+2

i=2,j=0->1
compare j,j+1

i,j=0->n-i-1
"""


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        atleast_one_swap = False
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j+1],array[j] = swap_arith(array[j], array[j+1])
                atleast_one_swap = True
        if not atleast_one_swap:
            break

"""
Insertion Sort
5,2,4,1,6

i=1
this_elem = 2
j=0
array[1] = 5
j=-1
array[0] = 2
2,5,4,1,6

i=2
this_elem = 4
j=1
array[2] = 5
j=0
array[1] = 4
2,4,5,1,6

i=3
this_elem = 1
j=2
array[3] = 5
j=1
array[2] = 4
j=0
array[1] = 2
j=-1
array[0] = 1
 
"""
def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        key = array[i]
        for j in range(i-1,-1,-1);
            if array[j]<=key:
                break
            array[j+1] = array[j]
        array[j+1] = key

"""
Divide and Conquer
merge: combine contents of 2 arrays in a sorted order
array = [8,7,5]

1. merge_sort(8,7,5):
    midpoint = 1
    merge(merge_sort(8),merge_sort(7,4))
        
        merge_sort(8) -> 8
        merge(8, merge_sort(7,5)
        
        merge_sort(7,5)
            midpoint = 0
            merge(merge_sort(7), merge_sort(5))
            merge_sort(7) -> 7
            merge_sort(5) -> 5
            merge(left=7,right=5)
                result = []
                right_idx = left_idx = 0
                result.append(5)
                
                right_idx = len(right)
                result.append(7)
                
                result = [5,7]
            [5,7]
        [5,7]
        merge(left=[8], right=[5,7])
            result = []
            left_idx = right_idx = 0
            result.append(5)
            left_idx = 0, right_idx = 1
            result.append(7)
            right_idx = 2 = le(right)
            result.append(8)
            result = [5,7,8]
        [5,7,8]
    [5,7,8]
"""

def merge(left, right):
    if len(left)==0:
        return right
    if len(right)==0:
        return left
    result = []
    right_idx = left_idx = 0
    while len(result) < len(left)+len(right):
        if right_idx == len(right):
            result.append(left[left_idx:])
            break
        if left_idx == len(left):
            result.append(right[right_idx:])
            break
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx]
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    return result

def merge_sort(array):
    if len(array)<2:
        return array
    midpoint = len(array) // 2
    return merge(merge_sort(left = array[:midpoint],\
                right = merge_sort(array[midpoint:])


"""
[8,7,5]

quicksort([8,7,5])
    pivot_index = 1
    pivot_elem = 7
    high = [8]
    same = [7]
    low = [5]
    return [5] + [7] + [8]

quicksort([8,7,5,1,10,8]
    pivot_index = 2
    pivot_elem = 5
    high = [8,7,10,8]
    same = [5]
    low = [1,0]
    quicksort([8,7,10,8]
        
"""
def quicksort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot_index = randint(0, len(array)-1)
    pivot_elem = array[pivot_index]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)
    
    return quicksort(low) + same + quicksort(high)    

def main():
    args = parse_my_args()
    if args.inp_array_len > MAX_INP_ARRAY_LEN:
        raise ValueError('Enter an integer less than {}. You entered {}'.format(MAX_INP_ARRAY_LEN, args.inp_array_len))
    print('ARRAY LEN - {}'.format(args.inp_array_len))
    
    inp_array = [randint(0,1000) for _ in range(args.inp_array_len)]
    start = time.time()
    bubble_sort(inp_array)                
    end = time.time()
    print('Bubble sort took {} seconds'.format(end - start))   

if __name__=="__main__":
    main() 
