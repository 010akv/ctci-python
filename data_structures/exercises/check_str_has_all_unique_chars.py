import argparse

MAX_INP_STR_LEN = 1024

class Args:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def parse(self):
        self.parser.add_argument('--inp_str',type=str,help='Cannot be more than 1024 chars')
        self.parser.add_argument('--case_sens',help='Whether or not the comparison is case sensitive', action='store_true')
        self.args = self.parser.parse_args()
        self.__validate()       
        return self.args 
    
    def __validate(self):
        if len(self.args.inp_str)>MAX_INP_STR_LEN:
            raise ValueError('inp_str must have less than 1024 characters. Your string has {}'.format(len(self.args.inp_str)))

class CheckStrCharsUnique:
    def __init__(self, case_sens=False):
        self.case_sens = case_sens
 
    def check(self, inp_str):
        if not self.case_sens:
            inp_str = inp_str.lower()            
        inp_str_chars = [char for char in inp_str]
        seen = []
        for char in inp_str:
            if char in seen:
                return False
            seen.append(char)
        return True

    def check_no_extra_ds(self, inp_str):
        if not self.case_sens:
            inp_str = inp_str.lower()
        for i,char in enumerate(inp_str):
            if char in inp_str[:i]+inp_str[i+1:]:
                
                

def main():
    arg_parser = Args()
    args = arg_parser.parse()
    print(args.case_sens,type(args.case_sens))
    check_str = CheckStrCharsUnique(case_sens = args.case_sens)
    all_unique = check_str.check(args.inp_str)
    if all_unique:
        print('All chars in this string are unique')
    else:
        print('Nope. This string has duplicates')



if __name__=="__main__":
    main()
