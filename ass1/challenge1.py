import fileinput
from base64 import b64encode, b64decode

def convert_hex_to_base64(input):
    return b64encode(bytes.fromhex(input)).decode()

def main():
    for input in fileinput.input():
        print(convert_hex_to_base64(input))
        
if __name__ == '__main__':
    main()