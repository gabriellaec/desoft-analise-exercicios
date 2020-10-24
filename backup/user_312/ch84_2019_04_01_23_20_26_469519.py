def inverte_dicionario(dicionario):
    contador=0
    lista_final = dict()
    for i in dicionario:
        if contador==0:
            lista_final[dicionario[i]]=[]
            lista_final[dicionario[i]].append(i)
        else:
            if dicionario[i] in lista_final:
                lista_final[dicionario[i]].append(i)
            else:
                lista_final[dicionario[i]]=[]
                lista_final[dicionario[i]].append(i)
    return lista_final
                