def classifica_lista(lista):
    if len(lista)<2:
        print('nenhum')
        return 'nenhum' 
    if lista[len(lista)-1]>lista[len(lista)]:
        print('decrescente')
        return 'decrescente'
    else:
        print ('crescente')
        return 'decrescente'