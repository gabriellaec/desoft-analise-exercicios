def eh_primo(maior):
    if maior == 1 or maior == 0:
        return False
    elif maior == 2:
        return True
    else:
        div = 2
        cont = 0
        while div < maior:
            if maior % div == 0:
                cont += 1
            div += 1
        if cont == 0:
            return True
        else:
            return False


def lista_primos(n):
    cont_teste = 0
    lista = []
    lista_modelo = [0] * n
    while len(lista) != len(lista_modelo):
        if eh_primo(cont_teste) == True:
            lista.append(cont_teste)
        cont_teste += 1

    return lista


def primos_entre(a, b):
    lista_1 = lista_primos(b)

    lista_final = [i for i in lista_1 if a <= i <= b]

    return lista_final


def maior_primo_menor_que(maior):
    lista_maior = primos_entre(1, maior)
    if maior <= 1:
        return -1
    else:
        return lista_maior[-1]
