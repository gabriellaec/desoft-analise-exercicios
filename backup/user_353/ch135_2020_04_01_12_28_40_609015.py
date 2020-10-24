def equaliza_imagem(k,ListaCores):
    ls = []
    i=0
    n=len(ListaCores)
    while i<=n-1:
        if(lista_cores[i]*k)>=255:
            ls.append(255)
        else:
            ls.append(ListaCores[i]*k)
            i+=1
        return ls
 