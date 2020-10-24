def lista_sufixos(a):
    i=0
    o=[]
    n=len(a)
    while i<=n:
        if a[i]== " ":
            o+=a[i:-3]
            i+=1
    return o