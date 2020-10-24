def interseccao_valores(dic1, dic2):
    result = []
    
    for value in dic1.values():
        if value in dic2.values() and value not in result:
            result.append(value)
    
    return result