def medias_por_inicial(dic):
    lista_notas={}
    for nome in dic.keys():
        letra = nome[0]
        nota = dic[nome]
        if letra in lista_notas.keys():    
            lista_notas[letra] = (lista_notas[letra] + nota)/2
        else:
            lista_notas[letra] = nota       
    return lista_notas
    