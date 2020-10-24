def insterseccao_valores(dic1,dic2):
    lista1=[]
    lista2=[]
    lista_final=[]
    for chave,valor in dic1.items():
        if not valor in lista1:
            lista.append(valor)
    for chave,valor in dic2.items():
        if not valor in lista2:
            lista2.append(valor)
     
    for elemento in lista1:
        if elemento in lista2:
            lista_final.append(elemento)
     
    return lista_final