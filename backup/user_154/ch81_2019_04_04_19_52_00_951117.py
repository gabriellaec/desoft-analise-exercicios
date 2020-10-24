def interseccao_valores(dic1, dic2):
    result = {}
    
    for key, value in dic1.items():
        if key in dic2 and di2[key] == value:
            result[key] = value
    
    return result