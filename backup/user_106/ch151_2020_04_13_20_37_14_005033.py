def classifica_lista(lista):
    i=0
    contador_c=0
    contador_d=0
    while i+1<len(lista):
        if lista[i+1]-lista[i]>0:
            contador_c+=1
        elif lista[i+1]-lista[i]<0:
            contador_d+=1
        i+=1
    if len(lista)<2:
        return 'nenhum'
    elif contador_c==len(lista)-1:
        return 'crescente'
    elif contador_d==len(lista)-1:
        return 'decrescente'
    else:
        return 'nenhum'