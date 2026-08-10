def calcular_imc(peso: float, altura: float) -> float:
    '''
    Retorna o calculo do imc
    :param peso: peso em quilos
    :param altura: altura em metros
    :return: peso / altura ** 2
    '''
    return peso / altura ** 2

print(calcular_imc(120, 1.85))

def eh_par(numero: int) -> bool:
    return numero % 2 == 0
print(eh_par(12))