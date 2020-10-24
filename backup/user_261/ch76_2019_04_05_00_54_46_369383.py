def aniversariantes_de_setembro(dicionario):
    anset={}
    for nome,data in dicionario.items():
        if "/09/" in data:
            anset[nome]=data
    
    return anset
