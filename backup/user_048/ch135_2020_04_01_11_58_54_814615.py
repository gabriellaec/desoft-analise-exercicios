def equaliza_imagem(lista,k):
    l=len(lista)
    liste=[]
    i=0
    while i <l :
        for i in lista:
            liste.append(i * k)
        i=i+1
    return liste