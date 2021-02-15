

decrescente = True
anterior = int(input("digite o primeiro numero da sequecnia"))

valor = 1
while valor != 0 and decrescente:
	valor = int(input("Digite um número da sequencia: "))
	if valor > anterior:
		decrescente = False
	anterior = valor

if decrescente:
	print("a sequencia está em ordem descrescente")
else:
	print("a sequencia nao esta em ordem decrescente")
