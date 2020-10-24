def aniversariante_de_setembro(a):
    z = {}
    for k,v in a.items():
        if v[4] == '9':
            z[k] = v
    return z