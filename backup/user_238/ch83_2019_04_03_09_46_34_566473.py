
def medias_por_inicial(entrada):
    di={}
    divisao={}
    for e in entrada:
        for x in [e]:
            letra=x[0]
            if letra not in di:
                di[letra]=entrada[e]
                divisao[letra]=1
            else:
                divisao[letra]+=1
                di[letra]+=entrada[e]
                di[letra]=di[letra]/divisao[letra]
    return di
entrada={'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}
print(medias_por_inicial(entrada))
