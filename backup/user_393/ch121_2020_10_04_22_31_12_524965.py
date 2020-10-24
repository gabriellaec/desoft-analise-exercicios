def subtracao_de_listas(lista1,lista2):
    lista= []
    i=0
    while i < len(lista1):
        a= 0
        while a < len(lista2):
            if lista1[i]== lista2[a]:
                lista1[i]= 'x'
                a= a + 1
            else:
                a= a + 1
        i= i + 1
    n= len(lista1)
    k= 0
    while k < n:
        if lista1[k] != 'x':
            lista.append(lista1[k])
        k= k +1
    return lista
            
        