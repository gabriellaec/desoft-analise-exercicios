def verifica_lista(numeros):
    if not numeros: return "misturado"
    par = numeros[0] % 2 == 0
    for n in numeros:
        if (n % 2 == 0) != 0:
            return "misturado"
    return "par" if par else "ímpar" 