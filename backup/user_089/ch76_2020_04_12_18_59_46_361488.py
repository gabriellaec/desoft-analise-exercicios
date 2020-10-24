def aniversariantes_de_setembro(dic):
    novo = {}
    nomes_datas = dic.values()
    i = 0
    for k,v in dic.items():
        if v[3] == '0' and v[4] == '9':
            novo[k] = v
            i += 1
            
    return novo
                
                
    