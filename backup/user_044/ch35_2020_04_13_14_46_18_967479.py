soma=0
x=True
while x:
    n=float(input("Digite um numero: "))
    if n==0:
        x=False
    else:
        soma+=n
print(soma)