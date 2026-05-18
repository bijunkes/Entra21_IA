# Crie um algoritmo que informe se um triângulo é equilátero, isósceles ou escaleno, ou se não é um triângulo

l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))

if (l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1):
    print("Não é triângulo")
else:
    if l1 == l2 == l3:
        print("Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Isósceles")
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("Escaleno")