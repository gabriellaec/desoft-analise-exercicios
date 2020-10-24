def agrupa_por_idade(dicionario):
    nomes=list(dicionario.keys())
    idades=list(dicionario.values())
    novo_dic={}
    i=0
    while i < (len(dicionario)):
        if idades[i]<=11:
            novo_dic[nomes[i]]='criança'
        elif 12<=idades[i]<=17:
            novo_dic[nomes[i]]='adolescente'
        elif 18<=idades[i]<=59:
            novo_dic[nomes[i]]='adulto'
        else:
            novo_dic[nomes[i]]='idoso'
        i+=1
return novo_dic


    