def aniversariantes_de_setembro(dic):
    c={}
    for nome,data in dic.items():
        if '/09/'in data:
            c[nome]=data
    return c