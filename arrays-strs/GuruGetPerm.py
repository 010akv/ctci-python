import time
"""
OVERALL:
- using a global variable permutations won't work always:
    - you are appending intermediate permutations (eg: ['ab'] for input_string='abcd') to the global list - incorrect
- the intermediate permutations always must be combined with the fixed_char. You are only doing it for a special case of len=3 using get_swapped_pair method


IMPROVEMENTS:
- get_swapped_pair and special case for len=2 are redundant. See anus_permute()
"""

def get_swapped_pair(two_letter_string, fixed_char=''):
    return [fixed_char + two_letter_string[0]+two_letter_string[1], fixed_char +  two_letter_string[1]+two_letter_string[0]]

def get_string_to_permute(input_text, fixed_index):
    return input_text[0:fixed_index] + input_text[fixed_index+1:]
count=0
def permute(input_text):
    global count
    count= count+1 
    permutations = list()
    string_to_permute = input_text
    if len(input_text) == 1:
        return input_text                                                   # all permutations must have same LEN as orig str. Do  not append intermediate 1,2 char strings to global list
    if len(input_text) == 2:
        return get_swapped_pair(input_text)
    for i in range(len(input_text)):                                        
        string_to_permute = get_string_to_permute(input_text,i)             
        intermediate_perms = permute(string_to_permute)                             # you are calling a separate method with redundant logic and index. Incorrect recursion stack 
        for p in range(len(intermediate_perms)):                                    # you need to combine the intermediate (smaller) perms with the fixed char always. You only did with len 3. 
            permutations.append(input_text[i]+intermediate_perms[p])                        # changing to local var permutations, only one method
    return permutations                                                             # it is important to return this list. For len 4 and above, this could be intermediate in recursive calls 




def anus_permute(input_text):
    global count
    count=count+1
    permutations = list()
    if len(input_text) == 1:
        return input_text
    for i in range(len(input_text)):
        intermediate_perms = anus_permute(input_text[:i]+input_text[i+1:])
        for p in range(len(intermediate_perms)):
            permutations.append(input_text[i]+intermediate_perms[p])
    return permutations





def do_permute(fixed_char, string_to_permute, permutations):
    print('do permute',string_to_permute)
    global count
    if len(string_to_permute) != 2:
        if count==len(string_to_permute):
            return
        current_string_to_permute = get_string_to_permute(string_to_permute, count)
        print('do permute,curr str to permute',current_string_to_permute)
        current_fixed_char = string_to_permute[count]
        print('do permute,curr fixed char',current_fixed_char)
            
        do_permute(current_fixed_char, current_string_to_permute, permutations)
    else:
        print('do permute appending',get_swapped_pair(string_to_permute,fixed_char))
        permutations.append(get_swapped_pair(string_to_permute,fixed_char))
        count = count+1
        return

inp_strs = ['ab','abc','abcd','abcde','abcdef', 'abcdefghij']

for inp_str in inp_strs:
    print(inp_str)
    start = time.time()
    permute(inp_str)
    print('Permute method took {} secs'.format(time.time()-start))
    print(count)
    count=0
    start = time.time()
    anus_permute(inp_str)
    print('anus_permute took {} secs'.format(time.time()-start))
    print(count)
    count = 0
