def aniversariantes_de_setembro(dict):
    novo_d = {}
    for k, v in dict.items():
        if v[4] == '9':
        	novo_d[k] = v