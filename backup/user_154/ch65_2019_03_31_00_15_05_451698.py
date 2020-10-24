def acha_bigramas(string):
    result = []
    
    for x in string:
        for y in string:
            if x == y or (x + y) in result:
                continue
            else:
                result.append(x + y)
     
    return result