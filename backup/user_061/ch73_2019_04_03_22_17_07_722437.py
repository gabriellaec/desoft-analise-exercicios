def remove vogais(palavra):
    vogais = ["a","e","i","o","u"]
    i = 0
    while i<len(palavra):
        if palavra[i] == vogais[i]:
            del palavra[i]
        i+=1
    return palavra