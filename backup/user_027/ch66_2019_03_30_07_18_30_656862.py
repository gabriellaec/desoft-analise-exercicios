def capitaliza(x):
    x = str(x)
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if alfabeto.find(x[0]) != -1:
        comeco = ALFABETO[alfabeto.find(x[0])]
        final = x[1:]
    elif ALFABETO.find(x[0]) != -1:
        return x
    return comeco + final