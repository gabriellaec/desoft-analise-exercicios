def traduz(lista_ing,dicio):
    lista_pt=[]
    for palavra in lista_ing:
        for key,value in dicio.items():
            if palavra==key:
                lista_pt.append(value)
    return lista_pt