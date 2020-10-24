def equaliza_imagem(k,lista_cores):
    ls = []
    i=0
    n=len(lista_cores)
    while i<=n-1:
        if(lista_cores[i]*k)>=255:
            ls.append(255)
        else:
            ls.append(lista_cores[i]*k)
            i+=1
        return lista_cores
 