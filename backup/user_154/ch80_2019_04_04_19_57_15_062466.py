def interseccao_chaves(dic1, dic2):
    result = []
    
    for key in dic1:
        if key in dic2 and key not in result:
            result.append(key)
    
    return result