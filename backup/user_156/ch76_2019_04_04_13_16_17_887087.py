def aniversariantes_de_setembro(dicionario):
    dicionario2={}
    
    for k,v in dicionario.itens():
        if v[4]=='9':
            dicionario2[k]=v
    return dicionario2