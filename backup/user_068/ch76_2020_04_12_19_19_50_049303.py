def aniversariantes_de_setembro(a):
    dicionario = {}
    for p,n in a.items():
        if n[3] == "0" and n[4] == '9':
            dicionario[p] = n
            
    return dicionario