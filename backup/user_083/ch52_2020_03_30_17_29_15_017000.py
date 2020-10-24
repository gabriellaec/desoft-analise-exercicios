lista1=[234,12,54,65]
lista2=[2,23,4,1]
zipped=zip(lista1,lista2)
lista_final=[]
for lista1,lista2 in zipped:
    lista_final=lista1*lista2
    print(lista_final)