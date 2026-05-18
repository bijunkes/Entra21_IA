# Crie um algoritmo que peça 4 notas, total de aulas e de presençar, e informe se o aluno está aprovado ou reprovado

n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))
n3 = int(input("Nota 3: "))
n4 = int(input("Nota 4: "))

aulas = int(input("Total de aulas: "))
presencas = int(input("Total de presenças: "))

media = (n1 + n2 + n3 + n4) / 4
frequencia = presencas / aulas

if media >= 7 and frequencia >= 0.75:
    print("Aprovado")
else:
    print("Reprovado")