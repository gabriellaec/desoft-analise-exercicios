lista1_menos_lista2=[]
def subtracao_de_listas (lista1,lista2):
    for i in lista1:
        if i not in lista2:
            lista1_menos_lista2.append(i)
    return lista1_menos_lista2