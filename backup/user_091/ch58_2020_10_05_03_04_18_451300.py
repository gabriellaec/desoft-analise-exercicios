def conta_a(palavra):
    i=0
    soma=0
    while i<len(palavra):
        if palavra[i]=='a':
            soma+=i
            i+=1
        else:
            i+=1
    return soma