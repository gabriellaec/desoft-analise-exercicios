def verifica_lista(lista):
    if len(lista) == 0:
        return "misturado"
    p = 0
    o = 0
    for i in lista:
        if (-1)**i > 0:
            p=p+1
        else:
            o=o+1
            
    if p == len(lista):
        return "par"
    elif o == len(lista):
        return "ímpar"
    else:
        return "misturado"