tamanho = int(input("tamanho da sequencia"))
produto = 1
i = 0
while i < tamanho:
	valor = int(input("digite um valor a ser somado: "))
	produto = produto * valor
	i = i + 1
print("o produto é: ", produto)

