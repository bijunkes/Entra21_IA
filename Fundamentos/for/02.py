# Crie um algoritmo que soma todos os npumeros de 1 a 10:
# soma = 0
# for i in range(1,11):
#     soma += i
# print(soma)

# Crie um algoritmo que exiba todos os números pares de 2 a 100
# for i in range(2,101,2):
#     print(i)

# Crie um algoritmo que exibe os números de 100 até 50
# for i in range(100,49,-1):
#     print(i)

# Crie um algoritmo que solicita um número inicial e um final, e exibe na tela os números entre os informados
inicial = int(input("Inicial: "))
final = int(input("Final: "))
print("Números entre", inicial, "e", final, ":")
for i in range(inicial, final+1):
    print(i)