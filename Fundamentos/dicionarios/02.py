ufs = {'SC': 'Santa Catarina',
       'PR': 'Paraná',
       'RS': 'Rio Grande do Sul'}

for chave in ufs.keys():
    print(chave)

for valor in ufs.values():
    print(valor)

for chave, valor in ufs.items():
    print(chave, '/', valor)

# Crie um dicionário com 5 nomes (chaves) e idades (valores)
# Ao final, exiba apenas os nomes com mais de 6 letras e idade acima de 60 anos
dicionario = {"Amanda": 59, "Bernanardo": 10, "Clarice": 68, "Denise": 99, "Eloa": 3}

print("Nomes com mais de 6 letras e com mais de 60 anos: ")
for chave, valor in dicionario.items():
    if len(chave) > 6 and valor > 60:
        print(chave)