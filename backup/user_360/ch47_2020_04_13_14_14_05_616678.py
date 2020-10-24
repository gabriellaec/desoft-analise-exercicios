def estritamente_crescente(lista):
    if lista == []:
        return []
    else:
        x = lista[0]
        lista2 = [x]
        for i in range(0,len(lista)-1):
            if lista[i+1] > x:
                x = lista[i+1]
                lista2.append(lista[i+1])
        return lista2