seq=[]
while seq[0]<=1000:
    if x%2==0:
        seq.append(x/2)
    else:
        seq.append(3*x+1)
    x=seq[-1]
return seq