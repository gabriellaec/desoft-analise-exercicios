def agrupa_por_idade(dicionario):
    nomes=list(dicionario.keys())
    idades=list(dicionario.values())
    novo_dic={}
    i=0
    while i < (len(dicionario)):
        if idades[i]<=11:
            novo_dic['criança']=nome[i]
        elif 12<=idades[i]<=17:
            novo_dic['adolescente']=nomes[i]
        elif 18<=idades[i]<=59:
            novo_dic['adulto']=nomes[i]
        else:
            novo_dic['idoso']=nomes[i]
        i+=1
    return novo_dic


    