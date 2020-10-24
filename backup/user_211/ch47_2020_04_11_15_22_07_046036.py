def estritamente_crescente(lista):
    crescente=[]
    i=1
    if len(lista)==0:
        return lista
    else:
        crescente.append(lista[0])
        while(i<len(lista)):
            if lista[i]>lista[i-1] and not lista[i] in crescente:
                crescente.append(lista[i])
            i+=1
        return crescente
