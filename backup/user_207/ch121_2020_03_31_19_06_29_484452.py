def subtracao_de_listas (lista1, lista2):
    i=0
    j=0
    listaC = []
    condicao = True
    while i< len(lista1):
        condicao = True
        while condicao:
            j=0
            if lista1[i] == lista2[j]:
               condicao = False
            else: 
                j +=1
            if j == len(lista2) -1:
                listaC.append (lista1[i])
            
        i +=1
    return listaC