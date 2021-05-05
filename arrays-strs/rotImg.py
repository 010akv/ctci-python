import os
import numpy as np
import argparse

ALLOWED_ROT_DIRS = ['clockwise','counter_clockwise']

def parse_my_args():
    parser= argparse.ArgumentParser()
    parser.add_argument('--inp_file')
    args = parser.parse_args()
    return args

def validate_args(args):
    if not os.path.exists(args.inp_file):
        raise FileNotFoundError('Enter a valid filepath. {} does not exits'.format(args.inp_file))


def read_inp(inp_file):
    with open(inp_file,'r') as f:
        return np.array([line.split() for line in f], dtype=np.int32)


def swap_in_place(a, b):
    a = a + b
    b = a - b 
    a = a - b
    return a, b   


"""
row 0 done -> col 0 -> done
row 1 done -> col 1 -> done
00 01 02
10 11 12
20 21 22
a, b = b, a
"""
def transpose(inp_array):
    num_rows = inp_array.shape[0]
    num_cols = inp_array.shape[1]
    for row in range(num_rows):
        for col in range(row, num_cols):
            inp_array[row][col], inp_array[col][row]  = swap_in_place(inp_array[row][col], inp_array[col, row])    
    return inp_array

"""
00 01 02
10 11 12
20 21 22

transpose
00 10 20
01 11 21
02 12 22

rot 90 deg (clockwise)
col 0 = row 2
00 10 20 = 20 21 22
01 11 21 = 10 11 12
02 12 22 = 00 01 02
col 1 = row 1
col 2 = row 0
20 10 00
21 11 01
22 12 02

for i in range(num_rows):
    for j in range(num_cols):
        new_col = num_cols - i - 1
        new_row = j

rot 90 deg (counter clockwise)
02 12 22
01 11 21
00 10 20
"""


def rotate_90_deg(inp_array, direction='clockwise'):
    if direction not in ALLOWED_ROT_DIRS:
        raise ValueError('direction must be one of'.format(','.join(ALLOWED_ROT_DIRS)))
    inp_array = transpose(inp_array)
    print('TRansposed:\n',inp_array)
    num_cols = inp_array.shape[1]
    if direction == 'clockwise':
        for i in range(inp_array.shape[0]):
            for j in range(inp_array.shape[1]//2):
                inp_array[i][j], inp_array[i][num_cols-j-1] = inp_array[i][num_cols-j-1], inp_array[i][j]    
    return inp_array

def main():
    args = parse_my_args()
    validate_args(args)
    inp_array = read_inp(args.inp_file)
    print(inp_array)
    clk_wise_90_inp_array = rotate_90_deg(inp_array)
    print(inp_array)
    counter_clk_90_inp_array = rotate_90_deg(inp_array, direction="counter_clockwise")
    print(inp_array)

if __name__=="__main__":
    main()
