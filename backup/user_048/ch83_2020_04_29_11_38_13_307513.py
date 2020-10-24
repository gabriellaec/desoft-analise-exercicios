def medias_por_inicial(dic):
    list_nomes=[]
    list_notas=[]
    list_vezes=[]
    lista_notas_final=[]
    for chaves,valores in dic.items():
        if chaves[0] not in list_nomes:
            list_nomes.append(chaves[0])
            list_notas.append(valores)
            list_vezes.append(1)
        else:
            list_notas[list_nomes.index(chaves[0])]=list_notas[list_nomes.index(chaves[0])]+valores
            list_vezes[list_nomes.index(chaves[0])]=list_vezes[list_nomes.index(chaves[0])]+1
    i=0
    while i < len(list_notas):
        lista_notas_final.append(list_notas[i]/list_vezes[i])
        i+=1
        
    return dict(zip(list_nomes,lista_notas_final))
            