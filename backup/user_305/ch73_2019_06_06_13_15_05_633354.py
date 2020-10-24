def remove_vogais(string):
    i = 0
    while i < len(string):
        if i == "a" and i == "e" and i == "i" and i == "o" and i == "u":
            del i
            i +=1
            print string
        