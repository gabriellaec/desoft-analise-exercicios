def classifica_lista(lista):
    ocorrencias1=0
    ocorrencias2=0
    for i in range(len(lista)-1):
        if lista[i+1]>lista[i]:
            ocorrencias1+=1
        elif lista[i+1]<lista[i]:
            ocorrencias2+=1     
    if ocorrencias1==len(lista):
        return 'crescente'
    elif ocorrencias2==len(lista):
        return 'decrescente'
    else:
        return 'nenhum'