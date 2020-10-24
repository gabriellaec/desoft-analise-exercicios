x = []
def numero_no_indice(x):
    i = 0
    while i <= len(x):
        if i == x[i]:
            return i
        i +=1