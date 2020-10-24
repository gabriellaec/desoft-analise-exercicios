def aniversariantes_de_setembro(dicionario):
    dicionario1={}
    lista1=[]
    for t,i in dicionario.itms():
        if i[4]=='8':
            dicionario1[t]=i
    return dicionario1
        
    