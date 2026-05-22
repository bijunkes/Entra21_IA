numeros = [1, 2, 4, 3, 5]
print(numeros)

# .append(item) -> Adiciona novo item ao final da lista
numeros.append(6)
print(numeros)

# .pop() -> Remove último item da lista
numeros.pop()
print(numeros)

# .pop(posicao) -> Remove item de posição específica
numeros.pop(1)
print(numeros)

# .count(item) -> Informa quantidade de repetições de um item na lista
print(numeros.count(6))

# .sort() -> Ordena itens
numeros.sort()
print(numeros)

# .sort(reverse=True) -> Ordena itens ao contário
numeros.sort(reverse=True)
print(numeros)

# .index(item) -> Retorna a posição de um item
print(numeros.index(3))

# .remove(item) -> Remove a primeira ocorrência do item
numeros.remove(1)
print(numeros)

# .reverse() -> Reverte os itens sem ordenar
numeros.reverse()
print(numeros)

# len(lista) -> Informa tamanho da lista (qtde de valores)
print(len(numeros))