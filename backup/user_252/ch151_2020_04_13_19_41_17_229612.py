def calssifica_lista(lista):
    i=1
    n=len(lista)
    while i<n:
        if lista[i-1]<lista[i]:
            return 'crescente'