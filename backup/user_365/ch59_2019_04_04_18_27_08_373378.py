def conta_a(palavra):
    i=0
    contagem=0
    while i<len(palavra):
        if palavra[i]=='a':
            contagem+=1
        i+=1
    return contagem
print(conta_a('abacate'))