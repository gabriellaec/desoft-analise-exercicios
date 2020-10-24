def capitaliza(palavra):
    i = palavra[0:1]
    f = palavra[1:]
    i = i.upper()
    f = f.lower()
    word = "".join([i,f])
    print(word)
    return word