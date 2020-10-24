def eh_primo (numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        div = 2
        cont = 0
        while div < numero:
            if numero % div == 0:
                cont += 1
            div += 1
        if cont == 0:
            return True
        else:
            return False

def verifica_primos(lista_numeros):
    dic = {}
    for num in lista_numeros:
        booleano = eh_primo(num)
        dic[num] = booleano

    return dic