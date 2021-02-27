largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

linha = 1

while  linha <= altura:

    print("#", end = "")
    coluna = 2

    while coluna < largura: 

        if linha == 1 or linha == altura or coluna == largura:
            print("#",end="")
        else:
            print(end = " ")

        coluna = coluna + 1

    print("#")

    linha = linha + 1