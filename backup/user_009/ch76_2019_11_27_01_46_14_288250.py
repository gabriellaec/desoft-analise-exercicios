def aniversariantes_de_setembro(dic):
    novo_dic = {}
    for k, v in dic.items():
        if v[2:4] == "07":
  	      novo_dic[k] = v
    return novo_dic