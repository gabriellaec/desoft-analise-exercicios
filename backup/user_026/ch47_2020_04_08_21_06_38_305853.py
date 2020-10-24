def estritamente_crescente(lista):
    if len(lista)==0:
        return lista
    
    i=len(lista)-1
    c=1
    t=0
    nova_lista = [0]
    nova_lista[0] = lista[0]
    
    while i != c:
        if lista[c] > nova_lista[t]:
            nova_lista.insert(c,lista[c])
            c+=1
            t+=1
        else:
            c+=1
    return nova_lista