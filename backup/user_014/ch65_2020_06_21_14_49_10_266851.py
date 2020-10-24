def capitaliza (string):
    i = 0
    while i < len(string):
        capitalizando =  string[0].upper() + string[1:i+1]
        i += 1
    return capitalizando