def classifica_lista(lista_numeros):
    i=0
    while i < len(lista_numeros):
        if lista_numeros[i+1]>lista_numeros[i]:
            print('crescente')
        elif lista_numeros[i+1]<lista_numeros[i]:
            print('decrescente')
        else:
            print('nenhum')
        
        
        
            