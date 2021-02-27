def computador_escolhe_jogada(n, m):
    compRemove = 1

    while compRemove != m:
        if (n - compRemove) % (m+1) == 0:
            return compRemove

        else:
            compRemove += 1

    return compRemove



def usuario_escolhe_jogada(n, m):
    jogada_valida = False

    while not jogada_valida:
        jogadorRemove = int(input('Quantas peças você quer tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()

        else:
            jogada_valida = True

    return jogadorRemove



def campeonato():
    numero_rodada = 1
    while numero_rodada <= 3:
        print()
        print('**** Rodada', numero_rodada, '****')
        print()
        partida()
        numero_rodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')



def partida():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    vezdocomp = False

    if n % (m+1) == 0:
        print()
        print('Voce começa!')

    else:
        print()
        print('Computador começa!')
        vezdocomp = True

    while n > 0:
        if vezdocomp:
            compRemove = computador_escolhe_jogada(n, m)
            n = n - compRemove
            if compRemove == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', compRemove, 'peças')

            vezdocomp = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jogadorRemove, 'peças')
            vezdocomp = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')


print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('Para jogar uma partida isolada aperte 1')

tipo_Partida = int(input('Para jogar um campeonato aperte 2'))



if tipo_Partida == 2:
    print()
    print('Campeonato selecionado!')
    print()
    campeonato()
else:
    if tipo_Partida == 1:
        print()
        partida()