def interseccao_valores(dict1, dict2):
    lista=[]
    lista1=[]
    lista2=[]
    for i in dict1:
        valor1=dict1[i]
        lista1.append(valor1)
    for e in dict2:
        valor2=dict2[e]
        lista2.append(valor2)
    for k in range(len(dict1)):
        for l in range(len(dict1)):
            if lista1[k]==lista2[l]:
                lista.append(lista1[k])
                
    return lista