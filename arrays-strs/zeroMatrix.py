import os
import numpy as np
import argparse


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


def zero_matrix(inp_array):
    print(inp_array[0])
    zero_row_ids = []
    zero_col_ids = []
    for i in range(inp_array.shape[0]):
        for j in range(inp_array.shape[1]):
            if inp_array[i][j]==0:
                zero_row_ids.append(i)
                zero_col_ids.append(j)    
    print(zero_row_ids, zero_col_ids)
    inp_array = [[0 if row_id in zero_row_ids or col_id in zero_col_ids else inp_array[row_id][col_id] for row_id in range(inp_array.shape[0])] for col_id in range(inp_array.shape[1])]
    return inp_array

def main():
    args = parse_my_args()
    validate_args(args)
    inp_array = read_inp(args.inp_file)
    inp_array = zero_matrix(inp_array)
    print(inp_array)


if __name__=="__main__":
    main()        
