import math
i = 1
exp = 3
div = 3    
som = 0
men = 0
def arcotangente(x,n):

    while i <= n:
        if i%2 == 0:
            som = som + (x**(exp)/div)
        if i%2 == 1:
            men = men + (x**(exp+2)/div+2) 
        div+=2
        exp+=2
        i +=1
    arc = -1*(x + som - men)*(math.pi/180)
    return arc