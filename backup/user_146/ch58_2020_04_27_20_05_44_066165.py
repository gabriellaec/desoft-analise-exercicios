def conta_a(s):
    i=0
    contador=0
    n=len(s)
    while i<n:
        if s[i]=='a':
            contador+=1
        i+=1
    return contador