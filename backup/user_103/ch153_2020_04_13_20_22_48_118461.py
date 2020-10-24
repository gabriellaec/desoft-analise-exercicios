def agrupa_por_idade(dicionario):
    nomes=list(dicionario.keys())
    novo_dic={}
    i=0
    while i < (len(dicionario)):
        if dicionario[i]<=11:
            novo_dic[nomes[i]]='criança'
        elif 12<=dicionario[i]<=17:
            novo_dic[nomes[i]]='adolescente'
        elif 18<=dicionario[i]<=59:
            novo_dic[nomes[i]]='adulto'
        else:
            novo_dic[nomes[i]]='idoso'
    i+=1
    return novo_dic
    