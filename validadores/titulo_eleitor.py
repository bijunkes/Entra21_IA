titulo = input("Informe o título de eleitor: ")

while True:
    if len(titulo) != 12:
        break

    soma1 = 0
    multiplicador1 = 2
    digito1 = 0
    for i in range(8):
        soma1 += multiplicador1 * int(titulo[i])
        multiplicador1 += 1

    resto = soma1 % 11
    if resto == 0 or resto == 1:
        digito1 = 0
    else:
        digito1 = 11 - resto

    soma2 = 0
    multiplicador2 = 7
    contador = 8
    for i in range(3):
        if i == 3:
            soma2 += multiplicador2 * digito1
        else:
            soma2 += multiplicador2 * int(titulo[contador])
        multiplicador2 += 1
        contador += 1

    print(soma2)



    break
