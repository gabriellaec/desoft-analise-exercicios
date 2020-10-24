def aniversariantes_de_setembro (aniversariantes):
    aniv_setembro ={}
    for nome, data in aniversariantes.items():
        if data[4] == '9':
            aniv_setembro[nome] = data
        
    return aniv_setembro