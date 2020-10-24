x=[1,2,3,4,5,-1,6,7,-2]
def zera_negativos (i):
    for i in x:
        if i < 0:
            x.remove(i)
            x.append(0)
            
    print(x)