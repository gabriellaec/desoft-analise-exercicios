def lista_sufixos(word):
    res = []
    i = 2
    while i < len(word):
        res.append(word[i:])
        i +=1
    return res