def agrupa_por_idade(dicionario):
    #listas a serem preenchida
    crianca=[]
    adolecente=[]
    adulto=[]
    idoso=[]
    #dicionario resposta
    Faixa_etária =  {'criança': crianca, 'adolescente': adolecente, 'adulto': adulto, 'idoso': idoso}
    #preenche as listas
    for i in dicionario:
        if dicionario[i] <= 11:
            crianca.append(dicionario[i])
        if dicionario[i] <11 and dicionario[i] <= 17:
             adolecente.append(dicionario[i])
        if dicionario[i] <17 and dicionario[i] <= 59:
             adulto.append(dicionario[i])
        if dicionario[i] <59:
             idoso.append(dicionario[i])
    return Faixa_etária