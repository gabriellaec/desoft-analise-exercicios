def mais_populoso(dicionario):
    lista = dicionario.keys()
    maiorP = 0
    nomeEstado = ''
    for estado in lista:
        populacoes = dicionario[estado].values()
        soma = 0
        for valor in populacoes:
            soma += valor
        if soma > maiorP:
            maiorP = soma
            nomeEstado = estado
    
        
    