def eh_crescente(lista):
    if len(lista)==0:
        return True
    else:
        j=lista[0]
        lista2=[j]
        i=0
        while i < (len(lista)-1):
            if lista[i+1]>j:
                j=lista[i+1]
                lista2.append(lista[i+1])
            i+=1
        if lista2==lista:
            return True
        else:
            return False