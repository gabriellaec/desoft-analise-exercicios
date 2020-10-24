def lista_sufixos(word):
    res = []
    i = 0
    while i < len(word):
        res.append(word[i:])
        i +=1
    return res