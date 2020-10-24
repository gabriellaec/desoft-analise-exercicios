def pos_arroba(x):
    y = list(x)
    i = 0
    j = 0
    while i <len(y):
        if y[i] == '@':
            j = i
        i+=1
    return j  

def nome_usuario(x):
    y = pos_arroba(x)
    return x[0:y]