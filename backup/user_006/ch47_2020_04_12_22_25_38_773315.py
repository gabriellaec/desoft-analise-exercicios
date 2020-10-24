def estritamente_crescente(lista1):
    i=0
    lista2=[]
    if len(lista1)>0:
        maxi=lista1[i]
        lista2.append(maxi)
        while i<(len(lista1)-1):
            if maxi<lista1[i+1]:
                maxi=lista1[i+1]
                lista2.append(maxi)        
            i=i+1
    return lista2