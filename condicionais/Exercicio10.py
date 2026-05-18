# Crie um algoritmo que faça o câmbio de moedas, peça para pedir o valor, a moeda dada e o a moeda deseja em troca

print("""
Moedas:
[D] Dólar
[R] Real
[E] Euro
[L] Libra""")

real_dolar = 5.02
real_euro = 5.85
real_libra = 6.79

entrada = input("Qual moeda você tem: ").upper()
saida = input("Qual moeda você deseja: ").upper()
valor = float(input("Quanto você deseja da moeda de saída: "))

valor_em_reais = 0

if entrada == "R" and saida == "R":
    valor_em_reais = valor
elif entrada == "D":
    valor_em_reais = valor * real_dolar
elif entrada == "E":
    valor_em_reais = valor * real_euro
elif entrada == "L":
    valor_em_reais = valor * real_libra

if saida == "R": #quer real
    print("Valor em reais: ", valor_em_reais)
elif saida == "D": #quer dolar
    print("Valor em dólares: ", valor_em_reais/real_dolar)
elif saida == "E": #quer euro
    print("Valor em euros: ", valor_em_reais/real_euro)
elif saida == "L": #quer libra
    print("Valor em libras: ", valor_em_reais/real_libra)




