def raiz(n,r=0):
    if n == 0:
        return r
    else:
        return raiz(n-(2*r+1),r+1)