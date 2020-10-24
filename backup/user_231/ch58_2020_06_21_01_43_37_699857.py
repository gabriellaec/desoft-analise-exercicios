def conta_a(str):
    i=0
    as=0
    while i<=len(str):
        if str[i]=='a':
            as +=1
            i+=1
        else:
            i+=1
    return as
        
        