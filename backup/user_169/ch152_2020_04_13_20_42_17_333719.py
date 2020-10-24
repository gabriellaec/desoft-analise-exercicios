def  verifica_preco(string,dicionario,dicionario2):
    
    if string in dicionario:
        if dicionario[string] in dicionario2:
            return dicionario2[dicionario[string]]
            