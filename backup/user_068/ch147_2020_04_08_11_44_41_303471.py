def mais_frequente(a):
     dicionario = {}
    for palavra in a:
        if palavra in dicionario.keys():
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    p = 0
    c = 0 
    for palavra, num in dicionario.items():
        if p < num:
            p = num
            c = palavra
            
    return c