# Crie uma função que receba 2 listas de números e retorne uma terceira lista com a multiplicacao delas

def multiplicar_listas(lista1: list, lista2: list) -> list | bool:

    if len(lista1) != len(lista2):
        return False
    else:
        lista3 = []
        for i in range(len(lista1)):
            lista3.append(lista1[i] * lista2[i])
    return lista3

lista1 = [3, 5, 2]
lista2 = [4, 2, 6]
print(multiplicar_listas(lista1, lista2))

# Crie uma função que recebe uma lista com os países que compõem um grupo da copa
# A funçao retorna uma lista contendo todos os confrontos daquele grupo

def gerar_lista_jogos(selecoes: list) ->list:
    confrontos = []
    for i in range (len(selecoes)):
        for j in range (i+1, len(selecoes)):
            confrontos.append(f'{selecoes[i]} x {selecoes[j]}')
    return confrontos

print(gerar_lista_jogos(['Brasil', 'Haiti', 'Marrocos', 'Escócia']))

