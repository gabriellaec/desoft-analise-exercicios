def conta_a(x):
    soma = 0
    for i in range(0, len(x)):
        if x[i] == 'a' or x[i] == 'A':
            soma +=1
    return(soma)