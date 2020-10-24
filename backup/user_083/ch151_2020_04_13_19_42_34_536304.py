def classifica_lista(lista):
    i=0
    while i < (len(lista)):
        if lista[i+1]>lista[i]:
            return 'Crescente'
            i+=1
        if lista[i+1]<lista[i]:
            return 'Decrescente'
            i+=1
        if lista[i+1]==lista[i] or lista[i+1]>lista[i]>lista[i+2] or (len(lista))<=2:
            return 'Nenhum'
            i+=1