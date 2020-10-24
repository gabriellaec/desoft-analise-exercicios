def interseccao_valores(valores):
    lista=[]
    valores1= dict1.values()
    valores2= dict2.values()
    for a in valores1 :
        for b in valores2:
            if a==b:
                lista.append(a)
    return lista