import argparse


def parse_my_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inp_str',typr=str,help='Enter a string to find if it is a permutation of palindrome')
    args = parser.parse_args()
    return args


"""
n = 3
3*get_fact(2)
3*2
6

n = 2
2*get_fact(1)
2*1
2
"""
def get_fact(n):
    if not n or n<=0 or not isinstance(n, int):
        return 0
    if n == 1:
        return n
    return n * get_fact(n-1)

"""
anu
aun
uan
una
nua
nau

nu
un


0 012 012 = j + (i)%(n_fact//2)
1 012 021 = (i)%(n_fact//2)
2 012 102
3 012 120
4 012 201
5 012 210
"""
def get_permuts(inp_str):
    if not inp_str or inp_str=='':
        return []
    n = len(inp_str)
    n_fact = get_fact(n)
    inp_str_list = inp_str.split('')
    permuts = []
    for i in range(n_fact):
        ids = []
        for j in range(len(inp_str_list)):
            if j==0:
                this_id = i % (n_fact//2)
            elif j==1:
            this_permut += str(inp_str_list[ids[j])
        permuts.append(this_permut)
        
       

def check_palindrome_permut(inp_str):
    if not inp_str or inp_str='':
        return False
    permuts = get_permuts(inp_str)
