def aniversariantes_de_setembro(d):
    dic_set = {}
    for nomes, data in d.items():
        if data[4] == "9":
            dic_set[nomes] = data
    return dic_set
        
        