def agrupa_por_idade(dicionario):
    i = 0
    lista_crianca = []
    lista_adolescente = []
    lista_adulto = []
    lista_idoso = []
    for i in dicionario:
        if dicionario[i] <= 11:
            lista_crianca.append(i)
        elif dicionario[i] > 11 and dicionario[i] < 18:
            lista_adolescente.append(i)
        elif dicionario[i] > 17 and dicionario[i]<60:
            lista_adulto.append(i)
        elif dicionario[i] > 59:
            lista_idoso.append(i)
    novo_dic = {'criança': lista_crianca, 'adolescente': lista_adolescente, 'adulto': lista_adulto, 'idoso':lista_idoso}
    return novo_dic