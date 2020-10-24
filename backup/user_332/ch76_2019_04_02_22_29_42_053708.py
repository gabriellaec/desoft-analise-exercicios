def aniversariantes_de_setembro(dic):
    setembro = {}
    for nome, data in dic.items():
        if(data[3:5] == '09'):
            setembro[nome] = data
    return setembro