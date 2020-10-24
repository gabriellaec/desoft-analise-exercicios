def numero_digitos(s):
    c = 0
    for e in s:
        if e.isdigit():
            c += 1
    return c