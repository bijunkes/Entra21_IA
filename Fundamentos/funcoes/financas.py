# def valor_futuro(valor: float, periodo: int, taxa:int) -> float:
#     return valor * (1 + (taxa / 100)) ** periodo
#
# valor = float(input("Valor: "))
# periodo = int(input("Periodo: "))
# taxa = int(input("Taxa: "))
#
# print(valor_futuro(valor, periodo, taxa))


numeros = [6,7,8,9,10,36]

def calcular_numeros(numeros: list) -> list:
    return {'maximo': max(numeros), 'minimo': min(numeros), 'soma': sum(numeros)}

print(calcular_numeros(numeros))
