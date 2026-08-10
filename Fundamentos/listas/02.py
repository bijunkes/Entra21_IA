# Crie um algoritmo que:
# Solicita quantos números quer armazenar
# Solicita os npumeros que serão armazenados
# Exibe todos ao final

tamanho = int(input("Quantidade de números para armazenar: "))
lista = []

for i in range(tamanho):
    valor = (int(input(f"Informe o valor [{i}]: ")))
    lista.append(valor)
print("Lista:", lista)

print(f"Soma dos valores: {sum(lista)}")
print(f"Máximo: {max(lista)}")
print(f"Mínimo: {min(lista)}")
print(f"Média: {sum(lista) / len(lista)}")