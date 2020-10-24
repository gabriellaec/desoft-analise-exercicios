def verifica_lista(lista):
    if len(lista) == 0:
        return "misturado"
    elif lista[0]%2 == 1:
        for i in lista:
            if i%2 == 0:
                return "misturado"
        return "ímpar"
    elif lista[0]%2 == 0:
        for i in lista:
            if i%2 == 1:
                return "misturado"
        return "par"