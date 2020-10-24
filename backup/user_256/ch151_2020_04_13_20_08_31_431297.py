def classifica_lista(lista):
    i = 1
    t = 0
    nova = []
    nova.append(lista[0])
    while len(lista)>=2:
        while i < len(lista):
            if lista[i] > nova[t]:
                return 'crescente'
            elif lista[i] < nova[t]:
                return 'decrescente'
    else:
        return 'nenhum'
        
        