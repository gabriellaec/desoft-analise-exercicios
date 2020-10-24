def conta_a(palavra):
    i=0
    soma=0
    while i<len(palavra):
        if palavra[i]=='a' or palavra[i]=='A':
            soma+=1
            i+=1
        else:
            i+=1
    return soma