# Crie um algoritmo que recebe cinco nomes e ao final retorna o nome mais comprido e os nomes que começam com vogal

nomes, nomes_vogal, maiores_nomes = [], [], ["",]

for _ in range(5):
    nome = input(f"Informe o nome: ")
    nomes.append(nome)

    if nome[0] in "aeiou":
        nomes_vogal.append(nome)

    if len(nome) > len(maiores_nomes[0]):
        maiores_nomes.clear()
        maiores_nomes.append(nome)
    elif len(nome) == len(maiores_nomes[0]):
        maiores_nomes.append(nome)

print(f"Maior(es) nome(s): {maiores_nomes}")
print(f"Nomes que iniciam com vogal: {nomes_vogal}")