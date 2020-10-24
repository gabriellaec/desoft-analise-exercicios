i = 2
h = 0
k = h
j = 0 
while i<1000:
    r = i
    if i!=1:
        if r%2==0:
            r = r/2
            h+=1
        elif r%2!=0:
            r = r*3+1
            h+=1
    if k<h:
        j=i
    i+=1