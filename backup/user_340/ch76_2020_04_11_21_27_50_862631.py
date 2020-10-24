def aniversariantes_de_setembro(dicionario):
    dicionario1={}
    for t,i in dicionario.items():
        if i[3]=='0' and i[4]=='8':
            dicionario1[t]=i
    return dicionario1
        
    