# while -> executa repetidamento até uma condição parar
# for -> executa número pré-definido de repetições

# # Equivalentes:
# numero = 1
# while numero <= 10:
#     print (numero)
#     numero += 1
#
# for i in range(1, 11):
#     print(i)

# Criar um algoritmo que recebe vários números e só para quando a soma deles for mais que 100

# Equivalentes:
soma = 0
while soma <= 100 and soma != 50:
    numero = int(input("Digite um número: "))
    soma += numero
print(soma)

soma = 0
while True:
    numero = int(input("Digite um número: "))
    soma += numero
    if soma == 50 or soma > 100:
        break
print(soma)