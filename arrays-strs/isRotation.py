"""
1.9 String Rotation:Assumeyou have a method isSubstringwhich checks if oneword is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
Hints: #34, #88, # 7 04
"""
import argparse 



def parse_my_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inp_str_1',help='Input string 1')
    parser.add_argument('--inp_str_2',help='Input string 2')
    args = parser.parse_args()
    return args


def validate_strs(str1, str2):
    if not str1 or not str2:
        raise ValueError('Both strings must be non-empty. You entered {} {}'.format(str1, str2))
    

def isSubstring(str1, str2):
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False


def isRotation(str1, str2):
    if len(str1) != len(str2):
        return False
    return isSubstring(str(str1+str1), str2)
        
    
def main():
    args = parse_my_args()
    validate_strs(args.inp_str_1, args.inp_str_2)    
    print('Let\'s see... Is either string a rotation of the other?',isRotation(args.inp_str_1, args.inp_str_2)) 


if __name__ == "__main__":
    main()
