def aniversariantes_de_setembro(dic):
    novo_dic = {}
    nomes = []
    nasc = []
    for k, v in dic.items():
        nomes.append(k)
        nasc.append(v)
        
    for i in range(len(nasc)):
        if nasc[i][3:5] == "09": 
            novo_dic[nomes[i]] = nasc[i]
    return novo_dic