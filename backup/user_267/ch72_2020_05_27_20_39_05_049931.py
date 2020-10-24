
def lista_caracteres(a):
    lista = []
    i=0
    while i < len(a):
        if a[i] not in lista:
            lista.append('{0}'.format(a[i]))
        i +=1
return lista
    
    