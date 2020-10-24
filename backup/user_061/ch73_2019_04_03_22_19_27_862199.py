def remove_vogais(palavra):
    vogais = ["a","e","i","o","u"]
    i = 0
    consoada = ''
    while i<len(palavra):
        if palavra[i] != vogais[i]:
            consoada.append(palavra[i])
        i+=1
    return consoada