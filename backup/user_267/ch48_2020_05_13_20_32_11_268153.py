def eh_crescente(lista):
    cresc = True
    for i in range(len(lista)-1):
        if lista[i] >= lista[i+1]:
            cresc = False
    return cresc 
