def aniversariantes_de_setembro(dicionario):
    dicionario2={}
    nome=''
    for k,v in dicionario.itens():
        if v[4]=='9':
            nome=k
            dicionario2[nome]=v
    return dicionario2