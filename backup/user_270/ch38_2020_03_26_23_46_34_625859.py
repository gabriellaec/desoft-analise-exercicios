def quantos_uns(n):
    k = 0
    t = 0
    word = str(n)
    while k < len(word)  :
        if word[k] == 1 :
            t += 1
        k += 1
    return t