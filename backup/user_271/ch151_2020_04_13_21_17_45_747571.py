def classifica_lista(lista):
    if len(lista)<2:
        return('nenhum')
    else: 
        crescente=0
        decrescente=0
        for i lista:
            if lista[i+1]>lista[i]:
                crescente+=1
            elif lista[i+1]<lista[i]:
                decrescente+=1
            i+=1
        if crescente!=0 and decrescente==0:
            return('crescente')
        elif crescente==0 and decrescente!=0:
            return('decrescente')  
        else:
            return('nenhum')
        