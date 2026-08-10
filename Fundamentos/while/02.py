# Crie um programa que recebe um número indeterminado de valores
# Ao final, exibe qual foi o maior valor
# Para parar o programa, o usuário informa "SAIR"

import sys

contador = 0

while True:
    entrada = input("Insira um valor: ")
    if entrada.lower() == "sair":
        break

    if contador == 0:
        maior = int(entrada)
    contador += 1

    if int(entrada) > maior:
        maior = int(entrada)

if contador > 0:
    print("Maior valor: ", maior)
else:
    print("Nenhum valor lançado")