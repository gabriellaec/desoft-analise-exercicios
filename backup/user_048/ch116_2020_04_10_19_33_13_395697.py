def raiz_quadrada(x):
    i=1
    r=0
    continua=True
    if x>2:
        while continua:
            l=x-i
            if x<i or l<i:
                continua=False
            else:
                r=r+1
            i=i+2 
    if x==1:
        return 1
    if x==2:
        return 2
    if x==0:
        return 0

             