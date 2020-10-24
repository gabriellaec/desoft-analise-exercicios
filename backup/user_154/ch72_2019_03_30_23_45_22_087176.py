def lista_caracteres(string):
    result = []
    
    for x in string:
        if x in result:
            continue
        result.append(x)
    return result