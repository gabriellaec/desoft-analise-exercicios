def interseccao_valores (x,y):
    interseccao=[]
    for valorx in x.values():
        for valory in y.values():
            if valorx==valory:
                interseccao.append(valorx)
    return interseccao