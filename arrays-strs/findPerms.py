import argparse


def parse_my_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inp_str',help='Enter an inout string to find permutations')
    args = parser.parse_args()
    return args

def fact(n):
    if n<0 or not isinstance(n,int):
        raise ValueError("Enter a positive integer")
    if n==0 or n==1:
        return n
    return n * fact(n-1)

def find_permuts(inp_str):
    if not inp_str:
        return ''
    if len(inp_str) == 1:
        return inp_str
    permuts = []
    n = len(inp_str)
    print('\nINPUT STRING:',inp_str,n)
    for i in range(n):
        this_permuts = find_permuts(inp_str[:i]+inp_str[i+1:])
        print('i=', i, 'this permuts=',this_permuts)
        for p in range(len(this_permuts)):
            permuts.append(inp_str[i]+this_permuts[p])
#            print(inp_str,'p=',p)
    print('permuts=',permuts)
    return permuts

def main():
    args = parse_my_args()
    permuts = find_permuts(args.inp_str)
    print('Input string:',args.inp_str)
    print(len(args.inp_str),len(permuts))
    print('Its permutations:',permuts)



if __name__=="__main__":
    main()
