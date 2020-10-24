def aniversariantes_de_setembro(dicionario):
    dicionario1={}
    for t,i in dicionario.items():
        if i[5]=='8':
            dicionario1[t]=i
    return dicionario1
        
    