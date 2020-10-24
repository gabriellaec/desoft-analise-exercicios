def quantos_uns(n):
    i=0
    soma_de_uns=0
    lista= str(n).split(',')
    while i<len(lista):
        if i==1:
            soma_de_uns+=1
    return soma_de_uns
print (quantos_uns)
        