def remove_vogais(x):
    vog = ['a', 'e', 'i', 'o', 'u']
    y = ''
    for i in range(len(x)):
        if x[i] not in vog:
            y+= x[i]
    return y