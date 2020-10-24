#t=(200/a)**0,5
def calcula_tempo(dic_a):
    lista_nomes=list(dic_a.keys())
    lista_aceleracao=list(dic_a.values())
    lista_tempo=[]
    for a in lista_aceleracao:
        t=(200/a)**(1/2)
        lista_tempo.append(t)
    dicionario=dict(zip(lista_nomes,lista_tempo))
    return dicionario
