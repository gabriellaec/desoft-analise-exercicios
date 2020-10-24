y=[]
def numero_no_indice(x):
    for i in range(0,x+1):
        if x[i]==i:
            y.append(i)
        else:
            None
    return y