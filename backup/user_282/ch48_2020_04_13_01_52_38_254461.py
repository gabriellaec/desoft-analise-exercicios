def eh_crescente(numeros):
    if numeros == sorted(numeros, key=int):
        return True
    else:
        return False