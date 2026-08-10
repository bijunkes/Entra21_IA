# Crie um algoritmo de Jokenpô

from random import randint

cabecalho = """ 
 ▄▄▄██▀▀▀▒█████   ██ ▄█▀▓█████  ███▄    █  ██▓███   ▒█████  
   ▒██  ▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █ ▓██░  ██▒▒██▒  ██▒
   ░██  ▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒▓██░ ██▓▒▒██░  ██▒
▓██▄██▓ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒▒██▄█▓▒ ▒▒██   ██░
 ▓███▒  ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░▒██▒ ░  ░░ ████▓▒░
 ▒▓▒▒░  ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒ ▒▓▒░ ░  ░░ ▒░▒░▒░ 
 ▒ ░▒░    ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░░▒ ░       ░ ▒ ▒░ 
 ░ ░ ░  ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░ ░░       ░ ░ ░ ▒  
 ░   ░      ░ ░  ░  ░      ░  ░         ░              ░ ░  
                                                            """
menu = """
Escollha sua opção:
[1] Pedra
[2] Papel
[3] Tesoura
"""

print(cabecalho)
opcao = int(input(menu))
valor = randint(1, 3)

opcaoString = ""
valorString = ""

if opcao == 1:
    opcaoString = "Pedra"
elif opcao == 2:
    opcaoString = "Papel"
elif opcao == 3:
    opcaoString = "Tesoura"

if valor == 1:
    valorString = "Pedra"
elif valor == 2:
    valorString = "Papel"
elif valor == 3:
    valorString = "Tesoura"

if 1 <= opcao <= 3:
    print("Jogada Válida")
    print("Opção do jogador: ", opcaoString)
    print("Opção do adversário: ", valorString)
    if opcao == valor:
        print("EMPATE")
    elif opcao == 1 and valor == 3 or opcao == 2 and valor == 1 or opcao == 3 and valor == 2:
        print("VITÓRIA")
    else:
        print("DERROTA")
else:
    print("Jogada Inválida")