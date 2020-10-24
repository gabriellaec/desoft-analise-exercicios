def interseccao_valores(d1, d2):
    lista1 = []
    lista2 = []
    lista = []
    
    for valores in d1.values():
        lista1.append(valores)
            
    for valores in d2.values():
        lista2.append(valores)
        for i in lista1:
            if i == lista2[-1]:
                lista.append(i)
    
    return lista