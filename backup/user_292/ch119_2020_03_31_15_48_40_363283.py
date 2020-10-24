def calcula_euler(x,n):
    soma=0
    tamanho=0
    valor=0
    while tamanho<n:
        tamanho+=1
        if tamanho>=0 and tamanho<1:
            soma=soma+valor
        elif tamanho>=1 and tamanho<2:
            valor=valor+1
            soma=soma+valor
        if tamanho>=2 and tamanho<3:
            soma=soma+valor*x
        else:
            f=n-1
            s=1
            while f>1:
                s=s*f
                f=f-1
                soma=soma+valor*(x**(n-1))/s
    return soma
print(calcula_euler(2,4))