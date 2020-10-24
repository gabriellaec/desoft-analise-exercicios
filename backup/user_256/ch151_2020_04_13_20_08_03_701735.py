def classifica_lista(lista):
    i = 1
    t = 0
    nova = []
    nova.append(lista[0])
    while len(lista)>=2:
        while i < len(lista):
            if valores[i] > nova[t]:
                return 'crescente'
            elif valores[i] < nova[t]:
                return 'decrescente'
    else:
        return 'nenhum'
        
        