
def aniversariantes_de_setembro(d):
    s = {}
    for i,n in d.items():
        if n[4] == '9':
            s[i] = n
    return s