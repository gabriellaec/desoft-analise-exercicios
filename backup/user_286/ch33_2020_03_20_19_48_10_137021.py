def eh_primo (numero):
    if numero == 1 or numero == 0:
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

def lista_primos(valor_max):
    lista = list(range(1 , valor_max + 1))
    lista_final = []
    for item in lista:
        if eh_primo(item):
            lista_final.append(item)

    return lista_final

def primos_entre(menor, maior):
    lista = lista_primos(maior)
    for item in lista:
        if item > menor:
            lista_final = lista_final.append(item)
        
    return lista_final