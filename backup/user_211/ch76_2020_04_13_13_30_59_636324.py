def aniversariantes_de_setembro(dicionario):
    desetembro={}
    for k,v in dicionario.items():
        if v[3]=="0" and v[4]=="9":
            desetembro[k] = v
        

    return desetembro
            