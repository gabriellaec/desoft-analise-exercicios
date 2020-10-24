lista1=[]
lista2=[]

def subtracao_de_listas (lista1, lista2):
    i=0
    while (i <= len(lista1)) and (i <= len(lista2)):
        for i in lista1[:] and i in lista2[:]:
            lista1.remove(i)
            i += 1
    return (lista1 + lista2) 