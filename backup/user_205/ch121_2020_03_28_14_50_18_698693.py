
def subtracao_de_listas(lista1,lista2):
    lista3 = []
    for i in range(len(lista1)):
        for i in range(len(lista2)):
            if lista1[i]==lista2[i]:
                pass  
            else:
                lista3.append(i)    		
    return lista3