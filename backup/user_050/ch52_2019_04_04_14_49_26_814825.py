def eh_crescente(lista):
    lista=[]
    contador = 0
    while len(lista) > contador:
        if lista[contador] > lista[contador-1]:
            contador += 1
            return True
        return False
        