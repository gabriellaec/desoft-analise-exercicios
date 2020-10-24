def PiWallis (n):
    i=1
    pisobre2=1
    while i<=n:
        if i%2!=0:
            pisobre2*=(i+1)/i
        elif i%2==0:
            pisobre2*=i/(i+1)
        i+=1
    return pisobre2*2