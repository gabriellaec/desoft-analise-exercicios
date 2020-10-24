def fatorial(n):
    resposta=1
    termo=0
    for i in range(1,n):
        termo=i+1
        resposta=resposta*termo
    return (resposta)