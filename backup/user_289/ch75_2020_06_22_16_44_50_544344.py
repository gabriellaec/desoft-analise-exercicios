def eh_primo (numero):
    if numero == 2:
        return True
    elif numero <= 0 or numero == 1:
        return False
    elif numero%2 == 0:
        return False
    else:
        contador = 3
        while contador < numero:
            if numero%contador == 0:
                return False
            contador += 2   
        return True   
def verifica_primos(lista):
    dicionario = dict()
    for numero in lista:
        if eh_primo(numero) == True:
            dicionario['numero'] = True
    return dicionario

lista = [1, 2, 3, 4, 5]
x = verifica_primos(lista)
print(x)