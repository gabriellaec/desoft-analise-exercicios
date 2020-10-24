def eh_crescente(l):
    crescente = True
    for i in range(1, len(l)):
        if l[i] <= l[i-1]:
            crescente = False
    return crescente