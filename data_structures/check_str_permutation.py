import argparse

MAX_STR_LENGTH = 1024

def parse_my_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inp_str_1',type=str,help='Enter a string up to {} chars in length'.format(MAX_STR_LENGTH))
    parser.add_argument('--inp_str_2',type=str,help="Enter a string up to {} chars in length".format(MAX_STR_LENGTH))
    parser.add_argument('--case_sens',action='store_true',help='Enter this to make the string comparison case sensitive')
    args = parser.parse_args()
    validate(args)
    return args

def validate(args):
    if len(args.inp_str_1)>MAX_STR_LENGTH or len(args.inp_str_2)>MAX_STR_LENGTH:
        raise ValueError("One or both of your input strings contain more than the max. allowed num. chars {}".format(MAX_STR_LENGTH))


class CheckStrsPermut:
    def __init__(self, inp_str_1,inp_str_2,case_sens=False):
        if not case_sens:
            inp_str_1 = inp_str_1.lower()
            inp_str_2 = inp_str_2.lower()
        self.str1 = inp_str_1
        self.str2 = inp_str_2

    def check_if_permutation(self):
        if not self.str1 or not self.str2:
            return False
        if len(self.str1) != len(self.str2):
            return False
        for str1_char in self.str1:                 #str1 = 'abcd', str1= 'dbca'
            if str1_char not in self.str2:
                return False
        return True
    
def main():
    args = parse_my_args()
    check_strs_permut = CheckStrsPermut(args.inp_str_1, args.inp_str_2, args.case_sens)
    result = check_strs_permut.check_if_permutation()
    if result:
        print('Yup, the two strings you entered are indeed permutations of each other!')
    else:
        print('Nope! The strings are NOT permutations of one another')


if __name__ == "__main__":
    main()
