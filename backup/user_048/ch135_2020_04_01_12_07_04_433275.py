
def equaliza_imagem(lista,k):
    l=len(lista)
    liste=[]
    i=0
    while i <l :
        for i in lista:
            y=i*k
            #
            if y>255:
                y=225
            liste.append(y)
        i=i+1
        
        
    return liste
