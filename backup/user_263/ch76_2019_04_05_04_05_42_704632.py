def aniversariantes_de_setembro(dic):
    setembreiros={}
    for nome,data in dic.items():
        if '/09/' in data:
            setembreiros[nome]=data
    return setembreiros