# matrix multiplication
def sqmatrixmul(m1, m2, w, mod):
	mr = [[0 for j in range(w)] for i in range(w)]
	for i in range(w):
		for j in range(w):
			for k in range(w):
				mr[i][j] =(mr[i][j]+m1[i][k]*m2[k][j])%mod
	return mr
