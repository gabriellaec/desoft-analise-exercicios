from functools import reduce
def encontra_maximo(x):
    lfinal=[]
    for e in x:
        lista=reduce(lambda x,y:x+y,x[e])
        lfinal.append(lista)
    a=reduce(lambda x,y:x+y,lfinal)