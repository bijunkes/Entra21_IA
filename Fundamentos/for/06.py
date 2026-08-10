# Fatorial
# Crie um algoritmo que recebe um número, e retorna o seu fatorial

n = int(input("Número: "))
m = 1
for i in range(1, n+1):
    m *= i
print(m)