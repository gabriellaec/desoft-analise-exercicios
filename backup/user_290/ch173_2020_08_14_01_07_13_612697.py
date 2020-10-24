def numero_digitos(s):
    num = 1
    for c in s:
        if c.isdigit() == True:
            num += 1
    return num