isbn = input("Informe o isbn: ")

if len(isbn) == 13:
    peso = 0
    soma = 0
    for i in range(12):
        if i % 2 == 0:
            peso = 3
        else:
            peso = 1
        soma += int(isbn[i]) * peso
    resto = soma % 10
    dv = 10 - resto
    if dv == 10:
        dv = 0

    if int(isbn[12]) == dv:
        print("Válido")
    else:
        print("Inválido")
else:
    print("Inválido")