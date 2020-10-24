def aniversariantes_de_setembro(dicionario):
    novo_dict={}
    for i in dicionario:
        if (dicionario[i][4]=="9"):
            novo_dict[i]=dicionario[i]
    return novo_dict
        