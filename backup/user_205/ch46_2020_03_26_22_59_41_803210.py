c=[]
def numero_no_indice(a):
    for i in range(len(a)):
        if i == a.index:
            c.append (i)
    return c
