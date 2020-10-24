def classifica_lista(lista):
    crescente = 0
    decrescente = 0
    if len(lista)<2:
        return 'nenhum'
    else:
        for i in range(1, len(lista)-1):
            if lista[i]-lista[i-1]>0:
                crescente+=1
            if lista[i]-lista[i-1]<0:
                decrescente+=1
        if crescente>0 and decrescente == 0:
            return 'crescente'
        elif decrescente>0 and crescente == 0:
            return 'decrescente'
        else:
            return 'nenhum'
                
            
               
