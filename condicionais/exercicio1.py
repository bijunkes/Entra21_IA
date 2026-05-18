# Crie um algoritmo que converta temperatura de Celsius para Fahrenheit e vice-versa

t = float(input("Temperatura: "))
u = input("Unidade (C/F): ").upper()

if u == "F":
    print((t - 32) * 5/9)
elif u == "C":
    print((t * 9 / 5) + 32)
else:
    print("Unidade inválida")