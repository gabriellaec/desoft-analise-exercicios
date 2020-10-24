i=1
j=1
arc=0
def arcotangente(x,n):
    if x >= -1 and x<=1:
        while j<n:
            arc = arc + (x**(i))/(i)
            i +=2
            return arc 
   