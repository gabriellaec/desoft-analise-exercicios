def classifica_lista (lista):
    i=0
    if len(lista) == 2:
        print ('nenhum')

    while i < len(lista):
        
        if lista[i+1]>lista[i]:
            return 'crescente'

        elif lista[i+1]<lista[i]:
            return 'decrescente'
        
        else:
            return 'nenhum'
        i+=1
        
     
    