def numero_digitos(s):
    n = []
    for i in s:
        t = i.isdigit()
        if t:
            n.append(i)
    return print(len(n))