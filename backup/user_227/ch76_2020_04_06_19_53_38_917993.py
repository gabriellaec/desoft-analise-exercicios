def aniversariantes_de_setembro(dicionario):
    setembro={}
    for nome,data in dicionario.items():
        if data[4]=="9":
            setembro[nome]=data
    return setembro