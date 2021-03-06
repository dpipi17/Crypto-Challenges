import fileinput
import codecs
import string

def isValid(ch):
    return (ch in string.ascii_lowercase) or (ch in string.ascii_uppercase) or ch == ' '

def single_character_xor(inputs):
    res = ''
    max_valid_char_num = 0
    for input in inputs[1:]:
        b = bytes.fromhex(input)
        
        for i in range(256):   
            curr_res = ''
            for x in b: 
                curr_res += chr(i ^ x)

            curr_valid_char_num = sum([1 if isValid(ch) else 0 for ch in curr_res])
            if curr_valid_char_num >= max_valid_char_num:
                res = curr_res
                max_valid_char_num = curr_valid_char_num
    return res

def main():
    inputs = []
    for line in fileinput.input():
        inputs.append(line.strip('\n'))
    
    print(single_character_xor(inputs))
    
if __name__ == '__main__':
    main()