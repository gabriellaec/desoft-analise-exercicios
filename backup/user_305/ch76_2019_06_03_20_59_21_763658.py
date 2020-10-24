def aniversariantes_de_setembro(dic):
    dic2 = {}
    for k,v in dic.items():
        if "/09/" in v:
            dic2[k] = v
        return dic2
            
