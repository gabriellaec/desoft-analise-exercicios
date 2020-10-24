def numero_digitos(s):
    num = 0
    for c in s:
        if c.isdigit() == True:
            num += 1
    return num