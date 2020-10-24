def aniversariantes_de_setembro(dicionario):
    dic={}
    for p,n in dicionario.items():
        if n[3]=="0" and n[4]=="9":
            dic[p]=n
            
    return dic