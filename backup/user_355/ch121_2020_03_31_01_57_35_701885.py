lista1=[0,2,4,6,8,10,12,14,16,18,20]
lista2=[0,3,6,9,12,15,18,21]
lista1_menos_lista2=[]
def subtracao_de_listas (lista1,lista2):
    for i in lista1:
        if i not in lista2:
            lista1_menos_lista2.append(i)
    return lista1_menos_lista2