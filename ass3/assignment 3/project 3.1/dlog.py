import math


table = {}
power_table = {}

def modular_power(a, b, p): 
	if (a == 0): 
		return 0
	
	if (b == 0): 
		return 1

	if (a, b) in power_table:
		return power_table[(a, b)]

	y = None
	if (b % 2 == 1): 
		y = a % p 
		y = (y * modular_power(a, b - 1, p) % p) % p 
	else: 
		y = modular_power(a, b / 2, p) 
		y = (y * y) % p

	power_table[(a, b)] = ((y + p) % p)
	return ((y + p) % p)

def gcd_extended(a, b):
	if a == 0:
		return (b, 0, 1)

	gcd, y, x = gcd_extended(b % a, a)
	return (gcd, x - (b // a) * y, y)

def inverse(a, p):
	gcd, x, _ = gcd_extended(a, p)
	assert gcd == 1, "No inverse found"
	return x % p

def fill_table(h, g, B, p):
	g_inverse = inverse(g, p)

	for x1 in range(B+1):
		table[(h * modular_power(g_inverse, x1, p)) % p] = x1

# Find x such that g^x = h (mod p)
# 0 <= x <= max_x
def discrete_log(g, h, p, max_x):
	
	x = None
	B = int(math.sqrt(max_x) + 1)
	fill_table(h, g, B, p)
	
	g_pow_b = modular_power(g, B, p)
	for x0 in range(B+1):
		right_side = modular_power(g_pow_b, x0, p)
		if right_side in table:
			x1 = table[right_side]
			x = x0 * B + x1
			break

	print x

def main():
	p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
	g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
	h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
	max_x = 1 << 40 # 2^40
	discrete_log(g, h, p, max_x)

if __name__ == '__main__':
	main()
