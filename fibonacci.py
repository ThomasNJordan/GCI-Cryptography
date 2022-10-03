# fibonacci calculator
def fib(x, mod):
	if x < 3: return 1
	x -= 2
	# find length of e in bits
	tst = 1
	siz = 0
	while x >= tst:
		tst <<= 1
		siz += 1
	siz -= 1
	# calculate the matrix
	fm = [
		# function matrix
		[0, 1],
		[1, 1]
	]
	rm = [
		# result matrix
		# (identity)
		[1, 0],
		[0, 1]
	]
	for i in range(siz, -1, -1):
		rm = sqmatrixmul(rm, rm, 2, mod)
		if (x >> i) & 1:
			rm = sqmatrixmul(rm, fm, 2, mod)

	# second row of resulting vector is result
	return (rm[1][0] + rm[1][1]) % mod
