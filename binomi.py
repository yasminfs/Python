def fatorial(n): 
	fat = 1
	while (n > 1):
		fat = fat * n
		n = n - 1
	return fat 
	

def numero_binomial(n, k):
	return fatorial(n) / (fatorial(k) * fatorial(n-k))


def testa_fatorial():
	if fatorial(1) == 1:
		print("funciona para 1")
	else:
		print("não funciona")
	if fatorial(2) == 2:
		print("funciona para 2")
	else:
		print("não funcoona") 
	if fatorial(0) == 1:
		print("funciona para 0")
	else:
		print("não funcoona")
