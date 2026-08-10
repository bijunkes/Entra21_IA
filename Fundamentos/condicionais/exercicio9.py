# Crie um algoritmo que informe se um nome começa com vogal ou consoante, e se possui início e fim iguais ou diferentes

nome = input("Nome: ").upper()
print(len(nome))
print(nome[-1])

p = nome[0]

if p == "a" or p == "e" or p == "i" or p == "o" or p =="u":
    print("Começa com vogal")
else:
    print("Começa com consoante")

if nome[0] == nome[-1]:
    print("Início e fim iguais")
else:
    print("Início e fim diferentes")