def aniversariantes_de_setembro(dicionario):
    aniversariantes_de_setembro={}
    for nome,data in dicionario.items():
        if "/09/" in data:
            aniversariantes_de_setembro[nome]=data
    
    return aniversariantes_de_setembro
