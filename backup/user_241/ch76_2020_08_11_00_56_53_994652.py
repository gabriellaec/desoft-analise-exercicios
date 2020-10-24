def aniversariantes_de_setembro(dic):
    dicionario = {}
    nomes = list(dic.keys())
    for nome in nomes:
        lista = dic[nome].split('/')
        if lista[1] == '09':
            dicionario[nome] = lista[0] + '/' + lista[1] + '/' + lista[2]
    return dicionario