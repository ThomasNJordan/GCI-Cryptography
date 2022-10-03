# Basic RSA Implementation

# encryption key "e"
# decryption key "d"
# message "m"

#(m^e)^d := m (mod n) -> explain number theory

# lambda(n) is a number such that x^lambda(n) := 1 (mod n)
# for any x such that gcd(x, n) = 1
# by this we know: x^a := x^b (mod n) if a := b (mod lambda(n))

# n = p*q
# By Fermat's little theorem:  lambda(p) = p - 1 and lambda(q) = q - 1

# e*d := 1 mod lambda(n)
# We assign e = 65537 (much smaller than actual keys)

# e*d + x*lambda(n) = gcd(e, lambda(n)) -> we can find d

# (e, n) -> (m^e) % n -> encrypted message
# (d, n) -> (m^d) % n -> decrypted message

# Notice how after the computation, p and q is lost, so to decrypt
# the message without p and q, you have to factor n

#######################################################################
# Execution Flow

# Key Generation:
# 1. Find random prime integers: p, q
# 2. Compute n = p * q and lambda(n) = (p - 1) * (q - 1)
# 3. Assign e to some arbitrary value, e = 35537
# 4. Compute d using Euclid's Extended Algorithm (GCD)

# Encryption:
# 1. Divide message into sections of 256 bits
# 2. Encrypt each section (m) as: (m^e) % n

# RSA intended decryption:
# 1. Divide message into sections of 256 bits
# 2. Decrypt each section (m) as: (m^d) % n
#######################################################################

from EEuclid import eucalg
from fibonacci import fibonacci
from genprime import genprime
from sqrtmatrixmul import sqrtmatrixmul
import rsa

def keysgen(p, q):
	n = p * q
	lambda_n = (p - 1) * (q - 1)
	e = 35537
	d = eucalg(e, lambda_n)[0]
	if d < 0: d += lambda_n
        # both private and public key must have n stored with them
	return {'priv': (d, n), 'pub': (e, n)}

def numencrypt(m, pub):
	return modpow(m, pub[0], pub[1])

def numdecrypt(m, priv):
	return modpow(m, priv[0], priv[1])

def encrypt_bytes(data, key):
	data = bytearray(data)
	cdata = bytearray()
	for i in range(0, len(data), 256):
		# read 256 bytes and store as long
		# to m
		m = 0
		for j in range(256):
			if i + j < len(data):
				m = (m << 8) + data[i + j]
			else:
				m <<= 8
		# encrypt m
		c = modpow(m, key[0], key[1])
		# store c into cdata
		for j in range(255, -1, -1):
			cdata.append((c >> (j * 8)) & 255)
	return bytes(cdata)

# both functions are essencially the same,
# the only difference is in which key you use
decrypt_bytes = encrypt_bytes
