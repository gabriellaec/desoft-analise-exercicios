def aniversariantes_de_setembro(dic_aniversariantes):
    dic_aniversariantes_setembro = {}
    for chave, valor in dic_aniversariantes.items(): 
        if (valor[3:5] == "09"):
            dic_aniversariantes_setembro[chave] = valor
    return dic_aniversariantes_setembro