def aniversariantes_de_setembro(l1):
    dicionario = {}
    for k,v in l1.items():
        a = l1[k]
        
        if a[3:5] == '09':
            dicionario[k] = v

    return dicionario