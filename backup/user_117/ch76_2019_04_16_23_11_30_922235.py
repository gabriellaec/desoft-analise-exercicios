aniversarios_setembro = {}

def aniversariantes_de_setembro (dict_aniversariantes):
    for k, v in dict_aniversariantes.items():
        if v[4] == '9':
            aniversarios_setembro[k] = v
    return aniversarios_setembro
                   
            