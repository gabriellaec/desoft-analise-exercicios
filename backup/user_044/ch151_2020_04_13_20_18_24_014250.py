def classifica_lista(lista):
    ocorrencias1=0
    ocorrencias2=0
    if len(lista)==0:
        return 'nenhum'
    else:
        for i in range(len(lista)):
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