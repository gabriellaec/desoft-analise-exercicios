def conta_a(palavra):
    contador=0
    n=len(palavra)
    for i in range(0,n):
        if palavra[i]=='a':
            contador+=1
    return contador