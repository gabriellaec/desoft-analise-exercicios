def traduz(lista,dicionario):
    traduzido = []
    
    for palavra in lista:
        traduzido.append(dicionario[palavra])
        
    return traduzido