def genprime(siz):
	while True:
		num = (1 << (siz - 1)) + secrets.randbits(siz - 1) - 10;
		# num must be 3 or 7 (mod 10)
		num -= num % 10
		num += 3 # 3 (mod 10)
		# heuristic test
		if modpow(2, num - 1, num) ==1 and fib(num + 1, num) ==0:
			return num
		num += 5 # 7 (mod 10)
		# heuristic test
		if modpow(2, num - 1, num) ==1 and fib(num + 1, num) ==0:
			return num
