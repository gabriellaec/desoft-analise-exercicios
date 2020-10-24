def aniversariantes_de_setembro(dicionario):
    niv_set={}
    for nome_e_data in dicionario.items():
        nome=nome_e_data[0]
        data=nome_e_data[1]
        if '/09/' in data:
            niv_set[nome]=data
    return niv_set
