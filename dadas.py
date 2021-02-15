n = int(input("digite um numero para calcular o fatorial"))
resultado = 1
count = 1

while count <= n:
	resultado = resultado * count
	count = count + 1
print("o fatorial ée",resultado)
