def eh_crescente(x):
    a=[]
    i=0
    while i<len(x):
        if a[i-1] < a[i]:
            return True
        else:
            return False
    i+=1
    