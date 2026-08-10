# Crie um algoritmo que recebe um nome e exibe ele de trás para frente, letra a letra
nome = input("Nome: ")
for i in range(len(nome)-1,-1,-1):
    print(nome[i])