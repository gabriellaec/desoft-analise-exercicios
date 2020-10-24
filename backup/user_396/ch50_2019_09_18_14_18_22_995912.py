
def numero_no_indice(x):
    i = 0
    y = []
    while i < len(x):
        if i == x[i]:
            y.append(i)
        i +=1
    return(y)
        