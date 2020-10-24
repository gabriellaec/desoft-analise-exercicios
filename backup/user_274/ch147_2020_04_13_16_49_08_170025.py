def mais_frequente(lista):
    dicio = {}
    for i in lista:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
    c = 0
    name = ""
    for tipo, i in dicio.items():
        if i > c:
            c=i
            name = tipo
        
    return name