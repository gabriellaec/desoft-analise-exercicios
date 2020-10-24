def estritamente_crescente(lista_inicial):
    lista_final=[]
    i=1
    if lista_inicial!=[]:
        lista_final.append(lista_inicial[0])
        while i<len(lista_inicial):
            if lista_inicial[i]>lista_final[-1]:
                lista_final.append(lista_inicial[i])
            i+=1
    return lista_final