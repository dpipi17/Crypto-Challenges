import fileinput
import codecs

def repeating_key_xor(key, plaintext):
    arr = []
    for i, ch in enumerate(plaintext):
        key_ch = key[i % len(key)]
        arr.append(ord(key_ch) ^ ord(ch))

    return codecs.encode(bytearray(arr), 'hex').decode('ascii')

def main():
    input = []
    for line in fileinput.input():
        input.append(line[:-1])

    key = input[0]
    plaintext = input[1]
    print(repeating_key_xor(key, plaintext))
    
if __name__ == '__main__':
    main()
        