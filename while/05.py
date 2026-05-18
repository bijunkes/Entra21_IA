from random import randint

while True:
    numero = int(input("Insira um número: "))
    aleatorio = randint(1, 3)

    if aleatorio == numero:
        print("Números iguais")
        break

    if aleatorio > numero:
        print("Seu número é menor")
    else:
        print("Seu número é maior")
