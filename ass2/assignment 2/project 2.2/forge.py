
from oracle import *
import sys

BLOCK_SIZE = 16


def xor(a, b):
	return "".join([chr(ord(x)^ord(y)) for (x, y) in zip(a, b)])

def get_two_block_mac(prev_mac, first_block, second_block):
    message = xor(prev_mac, first_block) + second_block
    
    tag = Mac(message, len(message))
    ret = Vrfy(message, len(message), tag)
    
    assert ret == 1, "Message verification failed."
    return tag


def print_verified_mac(message):
    prev_mac = "".join([chr(0)] * BLOCK_SIZE)
    
    result = ''
    for i in range(0, len(message), 2 * BLOCK_SIZE):
        mac = get_two_block_mac(prev_mac, message[i : i + BLOCK_SIZE], message[i + BLOCK_SIZE : i + 2 * BLOCK_SIZE])
        result = mac
        prev_mac = str(mac)
    
    print(result)

def main():
    if len(sys.argv) < 2:
        print "Usage: python forge.py <filename>"
        sys.exit(-1)
    
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    Oracle_Connect()
    print_verified_mac(data)
    Oracle_Disconnect()
        
if __name__ == '__main__':
    main()