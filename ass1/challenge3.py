import fileinput
import codecs

def single_byte_xor(input):
    b = bytes.fromhex(input)
    
    res = ''
    max_space_num = 0
    for i in range(256):   
        curr_res = ''
        for x in b: 
            curr_res += chr(i ^ x)
        
        curr_space_num = curr_res.count(' ')
        if curr_space_num >= max_space_num:
            res = curr_res
            max_space_num = curr_space_num
    
    return res

def main():
    for line in fileinput.input():
        print(single_byte_xor(line))
        
if __name__ == '__main__':
    main()
        
        