def classifica_lista(lista):
    if len(lista)<2:
        print('nenhum')
    i=1
    a=0
    lista_c=[]
    lista_c=[lista[0]]
    while i <len(lista):
        if lista[i]>lista_c[a]:
            lista_c.append(lista[i])
            a+=1
        i+=1
    lista_d=[]
    lista_d=[lista[0]]    
    j=1
    p=0
    while j<len(lista):
        if lista[j]<lista[p]:
            lista_d.append(lista[j])
            p+=1
        j+=1
        
    if lista_d==lista:
        return 'decrescente'
    elif lista_c==lista:
        return 'crescente'
    else:
        return 'nenhum'
            