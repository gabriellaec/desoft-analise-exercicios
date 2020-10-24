def subtracao_de_listas(lista1, lista2):
    resultado = lista1
    i = 0
    if len(lista1)==0:
        resultado=[]
    if len(lista2)==0:
        resultado=lista1
    for i in lista1[:]:
        if i in lista2:
            resultado.remove(i)
    print(resultado)
        