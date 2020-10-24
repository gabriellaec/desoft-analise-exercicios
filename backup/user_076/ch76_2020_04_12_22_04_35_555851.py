def aniversariantes_de_setembro (nomes_e_datas):
    nomes_e_datas = dict()
    for i in nomes_e_datas:
        if i[5]!=7:
            del nomes_e_datas[i]
    return nomes_e_datas