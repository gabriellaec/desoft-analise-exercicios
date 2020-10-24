def apaga_repetidos(string):
    a = string.split()
    b = []
    for i in a:
        if i not in b:
            b.append(i)
        else:
            b.append("*")
    x = reversed(b)
    return b
            
            
    