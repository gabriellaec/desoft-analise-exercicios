def eh_primo(numero):
    if numero < 2:
        return False
    contador = 2
    while contador < numero:
        if numero % contador == 0:
            return False
        contador += 1
    return True

def verifica_primos(lista):
    dicionario = {}
    contador = 0
    while contador < len(lista):
        dicionario[lista[contador]] = eh_primo(lista[i])
        contador += 1
    return dicionario