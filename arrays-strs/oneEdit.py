"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away. 
"""

import argparse

def parse_my_args():
    parser= argparse.ArgumentParser()
    parser.add_argument('--inp_str_1',help='Input string 1')
    parser.add_argument('--inp_str_2',help='Input string 2')
    args = parser.parse_args()
    return args


def check_one_away(s1, s2):
    num_edits = None
    if s1 == s2:
        return True
    if (s1 in s2 or s2 in s1) and abs(len(s1)-len(s2))==1:
        return True
    if len(s1)==len(s2):
        for i in range(len(s1)):
            s1 = list(s1)
            s2 = list(s2)
            part_s1 = ''.join(s1[:i]+s1[i+1:]) 
            part_s2 = ''.join(s2[:i]+s2[i+1:]) 
            print(i, list(s1), s1[:i],s1[i+1:],part_s1, part_s2)
            if part_s1 == part_s2:
                return True            
    return False

def main():
    args = parse_my_args()
    res = check_one_away(args.inp_str_1, args.inp_str_2)
    if res:
        print('The string is 1 or 0 edits away')
    else:
        print('NOPE! More than 1 edit away')


if __name__=="__main__":
    main()
