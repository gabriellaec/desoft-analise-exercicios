def classifica_lista(lista):
    if len(lista)<2:
        return('nenhum')
    else: 
        crescente=0
        decrescente=0
        i=0
        while i<len(lista): 
            if lista(i)>lista(i-1):
                crescente+=1
            elif lista(i)<lista(i-1):
                decrescente+=1
            i+=1
        if crescente==0 and decrescente!=0:
            return('crescente')
        elif crescente!=0 and decrescente==0:
            return('decrescente')  
        else:
            return('nenhum')
        