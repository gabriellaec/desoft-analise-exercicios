def aniversariantes_de_setembro(dicionario):
    anset={}
    for nome,data in dicionario.items():
        if data=="/09/":
            anset[nome]=data
    
    return anset
