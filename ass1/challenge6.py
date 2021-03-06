import string
import fileinput
from base64 import b64encode, b64decode

scores = {
    'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
    'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
    'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
    'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
    'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
    'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
    'y': .01974, 'z': .00074, ' ': .13000
}

def diff_bits(first_byte, second_byte):
    diff_bits = 0
    for i in range(8):
        ch1_i_bit = (1<<i) & first_byte
        ch2_i_bit = (1<<i) & second_byte
        if ch1_i_bit != ch2_i_bit:
            diff_bits += 1

    return diff_bits
    
def hamming_distance(first, second):
    return sum(diff_bits(first_byte, second_byte) for first_byte, second_byte in zip(first, second))
    
def isValid(ch):
    return (ch in string.ascii_lowercase) or (ch in string.ascii_uppercase) or ch in ' '

def find_key_size(text):
    res = 0
    min_score = -1
    
    for key_size in range(2, 41):
        
        counter = 0
        curr_score = 0
        for i in range(0, len(text) - 2 * key_size, key_size):
            first = text[i : i + key_size]
            second = text[i + key_size : i + 2 * key_size]
            curr_score += (1.0 * hamming_distance(first, second)) / key_size
            counter += 1
        
        curr_score /= counter
        if (curr_score < min_score or min_score == -1):
            res = key_size
            min_score = curr_score
    
    return res
    
def find_key(key_size, text_bytes):
    key = ''
    for key_ind in range(key_size):
        ch_res = ''
        max_valid_num = 0
        for i in range(256):
            curr_key_ind_range = [ind for ind in range(key_ind, len(text_bytes), key_size)]
            valid_ch_num = sum([scores.get(chr(i ^ text_bytes[ind]), 0) for ind in curr_key_ind_range])
            
            if (valid_ch_num > max_valid_num):
                ch_res = chr(i)
                max_valid_num = valid_ch_num
        key += ch_res
    return key
    
def main():
    inputs = []
    for line in fileinput.input():
        inputs.append(line.strip('\n'))
    
    text = bytes(''.join(inputs), 'utf_8')
    text_bytes = b64decode(text)
    key_size = find_key_size(text_bytes)
    key = find_key(key_size, text_bytes)
    
    res = ''
    for i, curr_byte in enumerate(text_bytes):
        key_ch = key[i % len(key)]
        res += chr(ord(key_ch) ^ curr_byte)
    print(res)
    
        
if __name__ == '__main__':
    main()