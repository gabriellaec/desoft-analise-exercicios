def aniversariantes_de_setembro(dicionario):
    setembro={}
    for nome in dicionario:
        string_data=dicionario[nome]
        if string_data[4]!=9:
            setembro[nome]=dicionario[nome]
    return setembro