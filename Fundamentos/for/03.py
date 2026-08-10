# Crie um algoritmo que recebe 10 números, e retorna:
# - A soma entre eles
# - A média aritmética simples
# - Quantos eram pares
# - Quantos eram ímpares
# - Quantos positovos
# - Quantos negativos
# - Quantos zeros
# - Maior valor
# - Menor valor

soma, pares, impares, positivos, negativos, zeros, maior, menor = 0, 0, 0, 0, 0, 0, 0, 0

for i in range(5):
    n = int(input("Número: "))
    soma += n

    if i == 0:
        maior, menor = n, n

    if n > maior:
        maior = n
    if n < menor:
        menor = n

    if n == 0:
        zeros += 1
    elif n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

    if n % 2 == 0:
        if n != 0:
            pares += 1
    else:
        impares += 1

print(f'''
Soma: {soma}
Média: {soma / 5}
Pares: {pares}
Ímpares: {impares}
Positivos: {positivos}
Negativos: {negativos}
Zeros: {zeros}
Maior: {maior}
Menor: {menor}
''')