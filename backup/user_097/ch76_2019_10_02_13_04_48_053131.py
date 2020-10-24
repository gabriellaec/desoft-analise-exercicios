def aniversariantes_de_setembro(dic_aniversariantes):
    dic_aniversariantes_setembro = {}
    for chave, valor in dic_aniversariantes.items(): # cria dois contadores, primeiro é chave, segundo é valor
        if (valor[3:5] == "09"): #Da posição 3 até a 5 (05, 09, etc) do item valor (cada par: nome, data)
            dic_aniversariantes_setembro[chave] = valor #dicionario na posicao 1, 2, 3, etc recebe valor inteiro, nome e data
    return dic_aniversariantes_setembro