def calcula_valor_devido(C,i,n):
    J=C((1+i)**n)-C
    return J
a=int(input('valor de C'))
b=int(input('valor de i'))
c=int(input('valor de n'))
print(calcula_valor_devido(a,b,c))


    