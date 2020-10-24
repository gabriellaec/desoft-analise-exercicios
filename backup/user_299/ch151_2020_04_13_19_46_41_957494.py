def classifica_lista(lista):
    crescente = True
    decrescente = True
    if len(lista)<2:
        return "nenhum"
    else:
        diferencas = []
        i = 0
        while i < len(lista):
            diferencas.append(lista[i+1]-lista[i])
            i = i+1
        for e in diferencas:
            if e > 0:
                decrescente = False
            elif e < 0:
                crescente = False
            
        if crescente and decrescente:
            return 'nenhum'
        elif crescente:
            return 'crescente'
        elif decrescente:
            return 'decrescente'