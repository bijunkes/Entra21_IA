def somar (a, b):
    return a + b

print(somar(3,5))

def menor_numero (a, b):
    if a < b:
        return a
    return b

print(menor_numero(3,5))

def comeca_com_vogal(texto):
    return texto[0].lower() in 'aeiou'