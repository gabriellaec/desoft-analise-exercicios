def conta_a(string):
    i=0
    m=0
    while i<len(string):
        if string[i]=='a':
            m=m+1
            i+=1
        else:
            i+=1
    return m
        