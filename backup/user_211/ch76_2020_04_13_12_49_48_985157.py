def aniversariantes_de_setembro(dicionario):
    desetembro={}
    for i in dicionario:
        for j in i.vallue:
            if j[3]==0 and j[4]==9:
                desetembro[i]=i.vallue
    return desetembro
            