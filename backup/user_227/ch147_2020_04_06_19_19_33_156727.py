def mais_frequente(lista):
    dicionario={}
    for palavra in lista:
        if not palavra in dicionario:
            dicionario[palavra]=lista.count(palavra)
    
    frequência=0
    for palavra in dicionario:
        if dicionario[palavra]>frequência:
            frequência=dicionario[palavra]
            palavra_mais_frequente=palavra
    return palavra_mais_frequente
        