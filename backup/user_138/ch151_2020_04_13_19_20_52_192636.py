def classifica_lista(lista):
    i=0
    for a in lista:
        if a[i]<a[i+1]:
            return 'crescente'
        elif a[i]>a[i+1]:
            return 'descrescente'
        else:
            return 'nenhum'