def bairro_mais_custoso(dic):
    for dic in total_do_semestre_por_bairro:
        k = dic.keys()
        v = dic.values()
        dic[k] = max(v)
    return print('o bairro mais custoso foi:',dic[k])