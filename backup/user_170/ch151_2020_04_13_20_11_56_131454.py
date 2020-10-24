def classifica_lista(lista):
    if len(lista) > 1 :
        crescentes = []
        decrescentes = []
        crescentes.append(lista[0])
        decrescentes.append(lista[0])
        m = lista[0]
        n = lista[0]
        for i in range(len(lista)-1):
            if m < lista[i+1]:
                m = lista[i+1]
                crescentes.append(lista[i+1])
        for i in range(len(lista)-1):
            if n > lista[i+1]:
                n = lista[i+1]
                decrescentes.append(lista[i+1])
        if crescentes == lista:
            return 'crescente'
        elif decrescentes == lista:
            return 'decrescente'
        else:
            return 'nenhum'
    else:
        return 'nenhum'