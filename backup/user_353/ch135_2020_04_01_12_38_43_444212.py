def equaliza_imagem(k,lista):
    ListaNova=[]
    i=0
    y=len(lista)
    while i<=(y-1):
        if(lista[i]*k)>=255:
            ListaNova.append(255)
        else:
            ListaNova.append(lista[i]*k)
            i+=1
        return ListaNova
 