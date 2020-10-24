def remove_vogais(string):
    string = str(string)
    string = string.lower()
    i = 0
    nova = ''
    vogais = ["a","e","i","o","u"]
    while i < len(string):
        if string[i] not in vogais:
            nova += string[i]
        i+=1
    return nova
