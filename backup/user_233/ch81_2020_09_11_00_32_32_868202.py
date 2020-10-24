
def interseccao_valores(dict1, dict2):
    
    valores = list()
    
    for valor in dict1.values():
        if valor in dict2.values(): valores.append(valor)
    
    return valores
    
    