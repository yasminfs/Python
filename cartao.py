meucartao = int(input("digite o numero do seu cartao"))

cartaolido = 1
encontreicartao = False
while cartaolido != 0 and not encontreicartao:
	cartaolido = int(input("digite o numer do prox cartao"))
	if cartaolido == meucartao:
		encontreicartao = True
if encontreicartao:
	print("oba")
else:
	print("cu")
