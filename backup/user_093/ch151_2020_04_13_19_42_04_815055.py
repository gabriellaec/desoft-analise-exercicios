def classifica_lista(lista):
    i=0
    if len(lista)<2:
        print('nenhum')
        
    while i <len(lista):
        if lista[i]<lista[i+1]:
            print('crescente')
        elif lista[i]>lista[i+1]:
            print('decrescente')
        else:
            print('nenhum')
        i+=1