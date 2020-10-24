def eh_primo(numero):
    if numero != 0 & numero != 1:
        if numero > 3:
            for i in range(2, numero):
                if numero % i == 0:
                    return False
        return True
    return False

print("É primo" if isprimo(12) else "Não é primo")