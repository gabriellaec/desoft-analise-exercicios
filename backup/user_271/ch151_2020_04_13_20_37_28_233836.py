def classifica_lista(lista):
    if len(lista)<2:
        return('nenhum')
    else: 
        tamanho=len(lista)
        crescente=0
        decrescente=0
        for i in lista: 
            if lista(i)>lista(i-1):
                crescente+=1
            elif lista(i)<lista(i-1):
                decrescente+=1
        if crescente=0 and decrescente!=0:
            return('crescente')
        elif crescente!=0 and decrescente=0:
            return('decrescente')    
        