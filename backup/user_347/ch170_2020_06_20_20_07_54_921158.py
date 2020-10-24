def apaga_repetidos(string):
    x = ""
    for a in string:
        if a not in x:
            x += a
        else:
            x += "*"
    return x
            
            
    