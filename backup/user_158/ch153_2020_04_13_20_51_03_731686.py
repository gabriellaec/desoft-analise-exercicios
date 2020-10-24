def agrupa_por_idade(dicionario):
    #listas a serem preenchida
    crianca=[]
    adolecente=[]
    adulto=[]
    idoso=[]
    #dicionario resposta
    Faixa_etária=  {'criança': crianca, 'adolescente': adolecente, 'adulto': adulto, 'idoso': idoso}
    #preenche as listas
    for k,v in dicionario.items():
        if v <= 11:
            crianca.append (k)
        elif v>11 and v<18:
            adolecente.append(k)
        elif v>17 and v<60:
            adulto.append(k)
        else:
            idoso.append(k)
    return Faixa_etária
