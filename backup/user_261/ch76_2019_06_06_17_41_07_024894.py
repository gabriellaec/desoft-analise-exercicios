def aniversariantes_de_setembro(dicionario):
    aniversariantes_de_setembro={}
    for nome,data in dicionario.items():
        if "/09/" in data:
            anset[nome]=data
    
    return aniversariantes_de_setembro
