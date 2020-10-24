def conta_a(str):
    i=0
    a=0
    while i<=len(str):
        if str[i]=='a':
            a +=1
            i+=1
        else:
            i+=1
    return a
        
        