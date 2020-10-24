def numero_digitos (s):
    i = 0
    for e in s:
        if e.isdigit() == True:
            i +=1
    return i