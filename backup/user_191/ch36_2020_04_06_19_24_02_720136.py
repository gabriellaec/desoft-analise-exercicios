def fatorial(n):
    mult=[]
    for i in range(n):
        a=n-i
        mult.append(a)
    for x in mult:
        res=1
        res=res*x
    return res