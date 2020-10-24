def aniversariantes_de_setembro(dicionario):
    dicionario1={}
    for t,i in dicionario.items():
        if i[4]=='9':
            dicionario1[t]=i
    return dicionario1
        
    