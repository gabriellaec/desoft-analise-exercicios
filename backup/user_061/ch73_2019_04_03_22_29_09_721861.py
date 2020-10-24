def remove_vogais(palavra):
    i = 0
    consoada = ''
    while i<len(palavra):
        if palavra[i] != ("a" or "e" or "i" or "o" or "u"):
            consoada += palavra[i]
        i+=1
    return consoada