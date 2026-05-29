from itertools import filterfalse

tabuleiro = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

contador = 0
opcao = ['X', 'O']

while True:
    for linha in tabuleiro:
        for coluna in linha:
            print(coluna, end=' ')
        print()

    jogo_finalizado = False
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i]:
            jogo_finalizado = True
            break
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]:
            jogo_finalizado = True
            break
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        jogo_finalizado = True
        break
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        jogo_finalizado = True
        break
    if jogo_finalizado:
        break

    while True:
        jogada = int(input("Qual jogada: "))
        if not jogada in range(1, 10):
            continue

        jogada_confirmada = False
        for i in range(3):
            for j in range(3):
                if jogada == tabuleiro[i][j]:
                    tabuleiro[i][j] = opcao[contador % 2]
                    jogada_confirmada = True
                    contador += 1
                    break
            if jogada_confirmada:
                break
        if jogada_confirmada:
            break

if jogo_finalizado:
    print("Jogo finalizado")

