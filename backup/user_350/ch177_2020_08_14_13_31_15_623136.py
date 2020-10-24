def numero_digitos(x):
    a = 0
    for i in x:
        if i.isdigit():
            a +=1
    return a