def nomeemail(n):
    i=0
    while i<len(n):
        if n[i]=='@':
            return n[:i]
        i+=1