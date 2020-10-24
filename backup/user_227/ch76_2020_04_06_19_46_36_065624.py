def aniversariantes_de_setembro(dicionario):
    for nome in dicionario:
        string_data=dicionario[nome]
        if stringa_data[4]!=9:
            del dicionario[nome]
    return dicionario