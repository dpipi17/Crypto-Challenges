from oracle import *
import sys
import copy

BLOCK_SIZE = 16

def get_padding_len(blocks, blocks_number): 
    before_last_block = blocks[blocks_number - 2][:]
    last_block = blocks[blocks_number - 1][:]

    for index in range(BLOCK_SIZE):
        before_last_block[index] += 1

        rc = Oracle_Send(before_last_block + last_block, 2)
        if rc == 0:
            return BLOCK_SIZE - index
   
    return BLOCK_SIZE

def decrypt_single_block(prev_block, curr_block, padding):
    guesses = [0] * BLOCK_SIZE
    for i in range(BLOCK_SIZE - padding, BLOCK_SIZE, 1):
        guesses[i] = padding
        
    for i in range(BLOCK_SIZE - padding - 1, -1, -1):
        prev_block_temp = copy.deepcopy(prev_block)

        new_padding = BLOCK_SIZE - i
        for j in range(i + 1, BLOCK_SIZE, 1):
			prev_block_temp[j] = prev_block_temp[j] ^ guesses[j] ^ new_padding
            
        for j in range(0, 256):
            prev_block_temp[i] = j
            
            rc = Oracle_Send(prev_block_temp + curr_block, 2)
            if rc:
				guesses[i] = new_padding ^ prev_block_temp[i] ^ prev_block[i]
				break
                
    return "".join([chr(b) for b in guesses])

def decrypt_chiphertext(blocks, blocks_number):
    padding = get_padding_len(blocks, blocks_number)
    decrypted_blocks = []

    for i in range(blocks_number - 1, 0, -1):
        decrypted_blocks.append(decrypt_single_block(blocks[i - 1], blocks[i], padding))
        padding = 0

    return "".join(reversed(decrypted_blocks)).strip()


def main():
    if len(sys.argv) < 2:
        print "Usage: python decipher.py <filename>"
        sys.exit(-1)
    
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    ctext = [(int(data[i:i+2], BLOCK_SIZE)) for i in range(0, len(data), 2)]
    blocks_number = len(ctext) / BLOCK_SIZE
    blocks = [ctext[i * BLOCK_SIZE : (i+1) * BLOCK_SIZE] for i in range(blocks_number)]
   
    Oracle_Connect()
    print(decrypt_chiphertext(blocks, blocks_number))
    Oracle_Disconnect()
        
if __name__ == '__main__':
    main()

