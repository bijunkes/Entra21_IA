# Crie um algoritmo que recebe um número e retorne se ele é primo ou não
# Para isso, precisa aprender break

# Estudar para próxima aula: while, break, continue

n = int(input("Número: "))

ehPrimo = True

if n <= 1:
    ehPrimo = False
else:
    for i in range(2, n):
        if n % i == 0:
            ehPrimo = False
            break

if ehPrimo:
    print("É primo")
else:
    print("Não é primo")