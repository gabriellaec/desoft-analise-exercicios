def soma_valores(n):
    num=len(n)
    i=0
    soma=0
    while i<num:
        soma=n[i]+soma
        i=i+1
    return soma
print(soma_valores([1,2]))