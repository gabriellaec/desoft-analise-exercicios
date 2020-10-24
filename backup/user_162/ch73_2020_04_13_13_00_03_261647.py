def remove_vogais(l):
    vogais = ["a", "e", "i", "o", "u"]
    for i in range(len(vogais)):
        l = l.replace(vogais[i],"")
    return l