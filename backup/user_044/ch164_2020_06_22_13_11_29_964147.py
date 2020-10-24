def traduz(lista,dict):
    ls = []
    for palavra in lista:
        for word,trad in dict.items():
            if word == palavra:
                ls.append(trad)
    return ls