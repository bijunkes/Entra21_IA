# n1 = input("Nome 1: ")
# n2 = input("Nome 2: ")
# n3 = input("Nome 3: ")
# n4 = input("Nome 4: ")
#
# media = len(n1 + n2 + n3 + n4) / 4
#
# if media <= 5:
#     print("Pequeno")
# elif media <= 7:
#     print("Médio")
# else:
#     print("Grande")

# nota = 7.5
# frequencia = 0.8
#
# if nota >= 7 and frequencia >= 0.7:
#     print ('APROVADO')

numero = int(input("Número: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("FIZZBUZZ")
elif numero % 3 == 0:
    print("FIZZ")
elif numero % 5 == 0:
    print("BUZZ")
