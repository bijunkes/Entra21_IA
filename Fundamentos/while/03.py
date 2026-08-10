# Crie um algoritmo que recebe um número indeterminado de valores
# Ao final, diz quantos números eram positivos e quantos eram negativos
# Para encerrar o programa, o usuário digita zero

positvos = 0
negativos = 0

while True:
    valor = int(input("Digite um valor: "))

    if valor == 0:
        break

    elif valor > 0:
        positvos += 1

    elif valor < 0:
        negativos += 1

print("Quantidade de positivos:" , positvos)
print("Quantidade de negativos: ", negativos)