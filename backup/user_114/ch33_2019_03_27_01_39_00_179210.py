def soma(i):
    y=1/(2**(i-1))
    f=0
    soma=1
    while f<i:
        soma=soma+y
        f=f+1
    return y
print(soma(100))