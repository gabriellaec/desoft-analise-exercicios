def remove_vogais(string):
    i = 0
    nova = ''
    vogais = ["a","e","i","o","u"]
    while i < len(palavra):
        if string[i] not in vogais:
            nova += string[i]
        i+=1
    return nova