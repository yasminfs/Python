n = int(input("digite um número inteiro positivo"))
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    n = int(input("digite um número inteiro positivo"))