def aniversariantes_de_setembro(dic):
    setembreiros={}
    for nome,data in dic.items():
        if '/09/' in datas:
            setembreiros[nome]=data
    return setembreiros