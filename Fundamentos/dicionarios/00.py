dicionario = {'nome': 'Bianca', 'idade': 18}
print(dicionario['nome'])
print(dicionario['idade'])
dicionario['signo'] = 'Leão'
dicionario['signo'] = 'Aquário'
dicionario.pop('nome') # Exclui chave
print(dicionario.get('nome')) # Caso não haja a chave, retorna None
print(dicionario.keys()) # Retorna as chaves
print(dicionario.values()) # Retorna os valores
