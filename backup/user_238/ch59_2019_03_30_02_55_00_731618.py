def conta_a(palavra):
    soma=0
    i=0
    while i < len(palavra):
        if palavra[i] == 'a':
            soma+=1
        i+=1
    return soma
print(conta_a('abelha'))