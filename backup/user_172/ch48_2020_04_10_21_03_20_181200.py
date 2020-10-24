def eh_crescente(lista):
    i = 0
    while i<len(lista)-1:
        if lista[i+1]>lista[i]:
            i+=1
            lista = a
        else:
            lista = b
    if lista == a:
        return True
    elif lista == b:
        return False