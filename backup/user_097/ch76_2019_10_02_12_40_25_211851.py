def aniversariantes_de_setembro(dic_aniversariantes):
    dic_aniversariantes_setembro = {}

    nomes = dic_aniversarios.keys()
    lista_nomes = []
    for i in nomes:
        lista_nomes.append(i)

    datas = dic_aniversarios.values()
    contador = 0
    for i in datas:
        if(i[4]=="9"):
            dic_aniversariantes_setembro[lista_nomes[contador]] = i
            contador = contador + 1
        else:
            contador = contador + 1
    return dic_aniversariantes_setembro