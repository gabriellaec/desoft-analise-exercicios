def calcula_euler(x,n):
    soma=0
    tamanho=0
    valor=0
    valorx1=x
    while tamanho<=n:
        if tamanho==0:
            soma=soma+valor
        elif tamanho==1:
            valor=valor+1
            soma=soma+valor
        elif tamanho==2:
            soma=soma+valorx1
        else:
            f=tamanho-1
            s=1
            while f>1:
                s=s*f
                f=f-1
                valor=valor*((x**(tamanho-1))/s)
                soma=soma+valor
        tamanho+=1
    return soma

            