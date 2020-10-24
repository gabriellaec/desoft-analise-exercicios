def classifica_lista(lista):
    n = len(lista)
    if n < 2:
        return 'nenhum'
    elif n == 2:
        a = 0
        if lista[a+1]>lista[a]:
            return 'crescente'
        elif lista[a+1]<lista[a]:
            return 'decrescente'
    elif n > 2: 
        for i in range (2,n):
            if lista[i]>lista[i-1] and lista[i-1]<lista[i-2] or lista[i]<lista[i-1] and lista[i-1]>lista[i-2]:
                return 'nenhum'
            elif lista[i-1]>lista[i-2]:
                return 'crescente'
            elif lista[i-1]<lista[i-2]:
                return 'decrescente'