# Crie um algoritmo que recebe vários nomes
# Ao final, exibe quantas letras foram digitadas
# Para parar, o usuário informa "PARAR'
from idlelib.help import copy_strip

letras = 0
vogais = 0

while True:
    nome = input("Digite um nome: ").lower()
    if nome == "parar":
        break

    for letra in nome:
        if letra != " ":
            letras += 1
            if letra in "aeiou":
                vogais += 1

    print("Quantidade de letras de", nome, ":", letras)
    print("Quantidade de vogais:", vogais)
    letras = 0
    vogais = 0

# Estudar REGEX em python