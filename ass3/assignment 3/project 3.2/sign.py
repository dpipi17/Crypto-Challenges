from oracle import *
from helper import *

N = 119077393994976313358209514872004186781083638474007212865571534799455802984783764695504518716476645854434703350542987348935664430222174597252144205891641172082602942313168180100366024600206994820541840725743590501646516068078269875871068596540116450747659687492528762004294694507524718065820838211568885027869
e = 65537
msg = "Crypto is hard --- even schemes that look complex can be broken"

def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)

    gcd, y, x = gcd_extended(b % a, a)
    return (gcd, x - (b // a) * y, y)

def inverse(a, p):
	gcd, x, _ = gcd_extended(a, p)
	assert gcd == 1, "No inverse found"
	return x % p

def main():
    msg_int_value = ascii_to_int(msg)

    Oracle_Connect()
    m1, m2 = 0, 0
    for i in range(2, 10000):
        if msg_int_value % i == 0:
            m1 = i
            m2 = msg_int_value // i
            break
    
    msg_sign = (inverse(Sign(1), N) * Sign(m1) * Sign(m2)) % N
    vrf = Verify(msg_int_value, msg_sign)
    assert vrf == 1, "Invalid signature"
    print msg_sign

    Oracle_Disconnect()

if __name__ == '__main__':
	main()
