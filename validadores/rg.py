rg = input("Informe o rg:")

if len(rg) == 9:
    peso = 2
    soma = 0
    for i in range(8):
        soma += int(rg[i]) * peso
        peso += 1

    resto = soma % 11
    dv = 11 - resto

    if dv == 10:
        dv = "X"

    if dv == 11:
        dv = 0

    dv = str(dv)

    if rg[8] == dv:
        print("Válido")
    else:
        print("Inválido")
else:
    print("Inválido")

