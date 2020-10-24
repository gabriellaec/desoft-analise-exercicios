def aniversariantes_de_setembro(dicionario):
    nomes_deta=nomes.values()
    i=0
    dicionario={}
    for k,v in dicionario.items():
        if v[3]=="0" and v[4]=="9":
            dicionario[k]=v
            i+=1
    return dicionario