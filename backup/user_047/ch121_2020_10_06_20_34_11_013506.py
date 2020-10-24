def subtracao_de_listas(x,y): 
    a = 0
    b = 0
    diferentes = []
    while a != len(x):
        if y[b]==x[a]:
                b+=1
        else:
            diferentes.append(y[b])
            b+=1
        if b == len(x):
            b = 0
            a +=1
    return diferentes