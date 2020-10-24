def aniversariantes_de_setembro(dic):
    setembro = dict()
    for chave,valor in dic.items():
        if valor[4] == "9":
       		setembro[chave] = valor
    return setembro
            
        