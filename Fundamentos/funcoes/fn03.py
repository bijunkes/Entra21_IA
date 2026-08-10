def eh_primo(numero: int) -> bool:
    if numero <= 1:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
    return True

print(eh_primo(2))