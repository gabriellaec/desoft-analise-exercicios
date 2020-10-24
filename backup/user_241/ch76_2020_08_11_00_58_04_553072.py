def aniversariantes_de_setembro(dic):
    dicionario = {}
    nomes = list(dic.keys())
    for nome in nomes:
        lista = dic[nome].split('/')
        if lista[1] == '09':
            dicionario[nome] = dic[nome]
    return dicionario