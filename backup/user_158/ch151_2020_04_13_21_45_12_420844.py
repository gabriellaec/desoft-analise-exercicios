def classifica_lista(lista):
    #desconsidera listas muito pequenas
    if len(lista) <=2 :
        return 'nenhum'
    #confere e clasifica as listas
    for i in range(len(lista)-1):
        #decrescente
        if lista[i+1] < lista[i]:
            return 'decrescente'
        #crescente
        elif lista[i+1] > lista[i]:
            return 'crescente'
        #calssifica listas constantes como nenhum
        else:
            return 'nenhum'