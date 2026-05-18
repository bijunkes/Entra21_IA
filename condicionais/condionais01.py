# operadores de comparação
# == igual
# > maior
# >= maior ou igual
# < menor
# <= menor ou igual
# != diferente

# nome = 'Bianca'
# nome2 = 'sla'
#
# if nome == nome2:
#     print('Iguais')
# else:
#     print('Diferentes')

# base = 10
# altura = 10
#
# if base == altura:
#     print("Quadrado")
# else:
#     print("Retângulo")

# v1 = int(input("Digite um valor: "))
# v2 = int(input("Digite outro valor: "))
#
# if v1 > v2:
#     print(v1, "é maior")
# elif v1 < v2:
#     print(v2, "é maior")
# else:
#     print("Iguais")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
media = (n1 + n2 + n3 + n4) / 4.0

print("Média: ", media)
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")