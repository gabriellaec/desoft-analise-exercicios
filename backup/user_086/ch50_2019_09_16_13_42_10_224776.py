listaiguais=[]
def numero_no_indice(lista):
    n=0
    while n<len(lista):
        if lista[n]==n:
            listaiguais.append(n)
        n+=1
    return listaiguais