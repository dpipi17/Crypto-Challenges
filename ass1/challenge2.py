import fileinput
import codecs

def fixed_xor(first, second):
    b1 = bytes.fromhex(first)
    b2 = bytes.fromhex(second)

    arr = []
    for x, y in zip(b1, b2):
        arr.append(x ^ y)

    return codecs.encode(bytearray(arr), 'hex').decode('ascii')

def main():
    input = []
    for line in fileinput.input():
        input.append(line)
    
    print(fixed_xor(input[0], input[1]))
        
if __name__ == '__main__':
    main()