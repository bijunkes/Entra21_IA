titulo = input("Informe o titulo de eleitor: ")

if len(titulo) != 12:
    print("Inválido")

else:
    contador1 = 2
    soma1 = 0
    for i in range(8):
        soma1 += int(titulo[i]) * contador1
        contador1 += 1

    modulo1 = soma1 % 11
    if modulo1 == 10:
        modulo1 = 0

    contador2 = 7
    contador3 = 8
    soma2 = 0
    for i in range(3):
        if i == 2:
            soma2 += modulo1 * contador2
        else:
            soma2 += int(titulo[contador3]) * contador2
            contador2 += 1
            contador3 += 1

    modulo2 = soma2 % 11
    if modulo2 == 10:
        modulo2 = 0

    if int(titulo[10]) == modulo1 and int(titulo[11]) == modulo2:
        print("Válido")
    else:
        print("Inválido")