cpf = input("Informe o cpf: ")

contador1 = 10
soma1 = 0
contador2 = 11
soma2 = 0

for i in range(9):
    soma1 += int(cpf[i]) * contador1
    contador1 -= 1

for i in range(10):
    soma2 += int(cpf[i]) * contador2
    contador2 -= 1

modulo1 = 11 - (soma1 % 11)
modulo2 = 11 - (soma2 % 11)

if modulo1 > 9:
    modulo1 = 0

if modulo2 > 9:
    modulo2 = 0

if int(cpf[9]) == modulo1 and int(cpf[10]) == modulo2:
    print("cpf válido")
else:
    print("cpf invalido")