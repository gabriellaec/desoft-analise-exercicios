def zera_negativos(lista_inteiros):
    i=0
    while i<lista_inteiros:
        if lista_inteiros[i]<0:
            lista_inteiros[i]=0
        i+=1