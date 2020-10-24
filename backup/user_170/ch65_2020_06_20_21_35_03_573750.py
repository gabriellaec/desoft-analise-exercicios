def capitaliza(palavra):
    i = palavra[0:1]
    f = palavra[1:]
    i = i.upper()
    f = f.lower()
    print(i+f)
    return i+f