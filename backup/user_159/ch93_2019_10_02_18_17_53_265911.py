v=0
def verifica_numero(x):
    z=str(x)
    for i in z:
        y=int(i)
        v+=y**2
    if v==x or x<1:
        n = True
    else:
        n = False
    return n
