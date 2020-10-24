import math
def arcotangente(x,n):
    i = 0
    pot = 1
    div = 1    
    mai = 0
    men = 0

    while i < n:
        if i%2 == 0:
            mai = mai + (x**(pot)/div)
        if i%2 == 1:
            men = men + (x**(3*pot)/div+2) 
        div+=4
        pot+=4
        i +=1
    arc = (mai - men)*(math.pi/180)
    return arc