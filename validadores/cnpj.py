cnpj = input("Informe o cnpj: ")

if len(cnpj) == 14:
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = 0
    for i in range(12):
        soma1 += int(cnpj[i]) * pesos1[i]

    resto1 = soma1 % 11
    if resto1 < 2:
        dv1 = 0
    else:
        dv1 = 11 - resto1

    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = 0
    for i in range(12):
        soma2 += int(cnpj[i]) * pesos2[i]
    soma2 += dv1 * pesos2[12]

    resto2 = soma2 % 11
    if resto2 < 2:
        dv2 = 0
    else:
        dv2 = 11 - resto2

    if int(cnpj[12]) == dv1 and int(cnpj[13]) == dv2:
        print("Válido")
    else:
        print("Inválido")

else:
    print("Inválido")