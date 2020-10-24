y=[]
def numero_no_indice(x):
    for i in len(x):
        if x[i]==i:
            y.append(i)
        else:
            None
    return y