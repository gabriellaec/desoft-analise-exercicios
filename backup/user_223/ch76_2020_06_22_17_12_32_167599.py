def aniversariantes_de_setembro(dicio):
    sept_dic = {}
    for k, v in dicio.items():
        v_lista = list(v)
        if v_lista[4] == 9:
            sept_dic[k] = v
    return sept_dic