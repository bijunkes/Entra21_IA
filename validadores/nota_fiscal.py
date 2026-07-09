nota = input("Informa a nota fiscal: ")

if len(nota) == 44:
    peso = 2
    soma = 0
    for i in range(43,-1,-1):
        soma += int(nota[i]) * peso
        peso += 1

        if peso > 9:
            peso = 2

    resto = soma % 11
    dv = 11 - resto
    if dv >= 10:
        dv = 0

    if int(nota[43]) == dv:
        print("Válida")
    else:
        print("Inválida")
else:
    print("Inválida")