
def aniversariantes_de_setembro(dicionario):

    dicionario2={}

    for i in dicionario:
        if dicionario[i][3]=='0' and dicionario[i][4]=='9':
            dicionario2[i]=dicionario[i]
    return dicionario2