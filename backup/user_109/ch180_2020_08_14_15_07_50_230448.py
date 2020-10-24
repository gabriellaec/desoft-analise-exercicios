def ocorrencias_letras(palavra):
    abcdario = 'abcdefghijklmnopqrstuvwxyz'
    dicionario = {}
    
    for i in range(len(abcdario)):
        if abcdario[i] in palavra:
            numero = palavra.count(abcdario[i])
            dicionario[abcdario[i]] = numero
            
    return dicionario