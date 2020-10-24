def remove_vogais(l):
    vogais = ["a", "e", "i", "o", "u"]
    for i in vogais:
        count = 0
        while count < len(l):
            if i == l[count]:
                del l[count]
            count+=1
    return l
            